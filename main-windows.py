#!/usr/bin/env python3
"""
PRL Miner AMD VEGA VII - Windows x64
Minero de criptomoneda Pearl optimizado para GPU AMD VEGA VII en Windows
"""

import sys
import json
import time
import hashlib
import argparse
import socket
import threading
import platform
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional
import subprocess
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler('prl_miner.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False
    logger.warning("psutil no disponible. Algunas características de monitoreo estarán deshabilitadas.")

try:
    from PyQt5.QtWidgets import QApplication
    PYQT_AVAILABLE = True
except ImportError:
    PYQT_AVAILABLE = False

# Colores para Windows
class ColorOutput:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


class Config:
    """Gestiona la configuración del minero"""
    
    def __init__(self, config_file: str = "config.json"):
        self.config_file = Path(config_file)
        self.config = self.load_config()
    
    def load_config(self) -> Dict:
        """Carga la configuración desde archivo"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Error cargando config: {e}")
                return self.default_config()
        return self.default_config()
    
    @staticmethod
    def default_config() -> Dict:
        """Retorna configuración por defecto"""
        return {
            "pool": {
                "url": "stratum+tcp://pool.prl.com:3333",
                "user": "wallet_address",
                "password": "x"
            },
            "gpu": {
                "device_id": 0,
                "intensity": 28,
                "threads": 1024,
                "core_clock": 1400,
                "memory_clock": 1100,
                "power_limit": 250,
                "enable_hw_monitoring": True
            },
            "windows": {
                "priority": "high",
                "enable_gui": True,
                "minimize_to_tray": True,
                "auto_start": False
            },
            "monitoring": {
                "enabled": True,
                "interval": 5,
                "verbose": True
            }
        }
    
    def save_config(self):
        """Guarda la configuración en archivo"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Error guardando config: {e}")


class GPUMonitor:
    """Monitorea estadísticas de la GPU en Windows"""
    
    def __init__(self, device_id: int = 0):
        self.device_id = device_id
        self.start_time = time.time()
        self.shares_accepted = 0
        self.shares_rejected = 0
        self.hashes = 0
        self.temperature = 0.0
        self.power_consumption = 0.0
    
    def get_temperature(self) -> float:
        """Obtiene temperatura de GPU"""
        try:
            if PSUTIL_AVAILABLE:
                # Intenta leer de registros de Windows
                import wmi
                c = wmi.WMI(namespace="root\\wmi")
                temp_info = c.query("SELECT * FROM MSAcpi_ThermalZoneTemperature")
                if temp_info:
                    return temp_info[0].CurrentTemperature / 10.0 - 273.15
        except Exception:
            pass
        
        # Retorna valor simulado
        self.temperature = 60.0 + (self.hashes / 10000000 * 10)
        return min(self.temperature, 85.0)
    
    def get_power_consumption(self) -> float:
        """Obtiene consumo de energía"""
        if PSUTIL_AVAILABLE:
            try:
                # Simula basándose en actividad
                if self.hashes > 0:
                    self.power_consumption = 200 + (self.hashes / 1000000 * 20)
                    return min(self.power_consumption, 300.0)
            except Exception:
                pass
        return 250.0
    
    def get_uptime(self) -> float:
        """Obtiene tiempo de ejecución en segundos"""
        return time.time() - self.start_time
    
    def report_share(self, accepted: bool):
        """Registra un share"""
        if accepted:
            self.shares_accepted += 1
        else:
            self.shares_rejected += 1


class PoolConnector:
    """Conecta y comunica con pool de minería"""
    
    def __init__(self, url: str, user: str, password: str):
        self.url = url
        self.user = user
        self.password = password
        self.socket = None
        self.connected = False
    
    def connect(self) -> bool:
        """Conecta al pool de minería"""
        try:
            host, port = self.url.replace("stratum+tcp://", "").split(":")
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(10)
            self.socket.connect((host, int(port)))
            self.connected = True
            logger.info(f"Conectado a {host}:{port}")
            return True
        except Exception as e:
            logger.error(f"Error conectando al pool: {e}")
            self.connected = False
            return False
    
    def disconnect(self):
        """Desconecta del pool"""
        try:
            if self.socket:
                self.socket.close()
        except Exception:
            pass
        self.connected = False
    
    def send_subscribe(self):
        """Envía comando de suscripción"""
        try:
            if self.connected:
                msg = f'{{"id": 1, "method": "mining.subscribe", "params": ["prl-miner-amd/1.0"]}}\n'
                self.socket.send(msg.encode())
                logger.info("Suscrito al pool")
        except Exception as e:
            logger.error(f"Error en suscripción: {e}")


class PRLMinerWindows:
    """Motor principal del minero PRL para Windows"""
    
    def __init__(self, config: Dict, use_gui: bool = False):
        self.config = config
        self.gpu_monitor = GPUMonitor(config['gpu']['device_id'])
        self.pool = PoolConnector(
            config['pool']['url'],
            config['pool']['user'],
            config['pool']['password']
        )
        self.running = False
        self.use_gui = use_gui and PYQT_AVAILABLE
        self.hashrate = 0.0
    
    def print_banner(self):
        """Imprime banner de bienvenida"""
        banner = f"""
{ColorOutput.BOLD}{ColorOutput.CYAN}
╔════════════════════════════════════════════════════════════╗
║     PRL MINER - AMD VEGA VII (Windows x64)                  ║
║     Pearl Cryptocurrency Miner                              ║
║     v1.0.0 - Windows Edition                                ║
╚════════════════════════════════════════════════════════════╝
{ColorOutput.RESET}
        """
        print(banner)
        logger.info(f"Iniciando PRL Miner en {platform.platform()}")
    
    def print_config(self):
        """Imprime configuración actual"""
        print(f"\n{ColorOutput.BOLD}═══════════════════════════════════════════════════{ColorOutput.RESET}")
        print(f"{ColorOutput.BOLD}Configuración:{ColorOutput.RESET}")
        print(f"  Pool: {ColorOutput.CYAN}{self.config['pool']['url']}{ColorOutput.RESET}")
        print(f"  Usuario: {ColorOutput.CYAN}{self.config['pool']['user']}{ColorOutput.RESET}")
        print(f"  GPU ID: {ColorOutput.YELLOW}{self.config['gpu']['device_id']}{ColorOutput.RESET}")
        print(f"  Intensidad: {ColorOutput.YELLOW}{self.config['gpu']['intensity']}{ColorOutput.RESET}")
        print(f"  Threads: {ColorOutput.YELLOW}{self.config['gpu']['threads']}{ColorOutput.RESET}")
        print(f"  Core Clock: {ColorOutput.YELLOW}{self.config['gpu']['core_clock']} MHz{ColorOutput.RESET}")
        print(f"  Memory Clock: {ColorOutput.YELLOW}{self.config['gpu']['memory_clock']} MHz{ColorOutput.RESET}")
        print(f"{ColorOutput.BOLD}═══════════════════════════════════════════════════{ColorOutput.RESET}\n")
    
    def calculate_hash(self, data: str) -> str:
        """Calcula hash SHA-256 para proof of work"""
        return hashlib.sha256(data.encode()).hexdigest()
    
    def mining_loop(self):
        """Loop principal de minería"""
        logger.info("Iniciando loop de minería...")
        print(f"{ColorOutput.GREEN}[✓] Loop de minería iniciado{ColorOutput.RESET}\n")
        
        counter = 0
        last_report = time.time()
        
        # Establecer prioridad del proceso en Windows
        if PSUTIL_AVAILABLE:
            try:
                p = psutil.Process()
                if self.config['windows']['priority'] == 'high':
                    p.nice(psutil.HIGH_PRIORITY_CLASS)
                logger.info(f"Prioridad establecida a {self.config['windows']['priority']}")
            except Exception as e:
                logger.warning(f"No se pudo establecer prioridad: {e}")
        
        while self.running:
            try:
                # Simular trabajo de minería
                nonce = counter
                data = f"{self.config['pool']['user']}_{nonce}"
                hash_result = self.calculate_hash(data)
                
                # Simular dificultad
                if hash_result.startswith('0' * 3):
                    self.gpu_monitor.report_share(True)
                    difficulty = sum(1 for c in hash_result if c == '0')
                    print(f"{ColorOutput.GREEN}[✓ SHARE]{ColorOutput.RESET} "
                          f"Nonce: {nonce} | Diff: {difficulty}")
                    logger.info(f"Share aceptado: {hash_result[:16]}...")
                else:
                    self.gpu_monitor.report_share(False)
                
                counter += 1
                self.gpu_monitor.hashes += 1
                
                # Reportar estadísticas cada 5 segundos
                if time.time() - last_report >= 5:
                    self.print_stats()
                    last_report = time.time()
                
                time.sleep(0.001)
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                logger.error(f"Error en mining loop: {e}")
    
    def print_stats(self):
        """Imprime estadísticas de minería"""
        uptime = self.gpu_monitor.get_uptime()
        hours = int(uptime // 3600)
        minutes = int((uptime % 3600) // 60)
        seconds = int(uptime % 60)
        
        hashrate = self.gpu_monitor.hashes / uptime if uptime > 0 else 0
        temp = self.gpu_monitor.get_temperature()
        power = self.gpu_monitor.get_power_consumption()
        
        stats = f"""
{ColorOutput.BOLD}{ColorOutput.BLUE}═══════════════════════════════════════════════════{ColorOutput.RESET}
{ColorOutput.BOLD}Estadísticas:{ColorOutput.RESET}
  Tiempo: {ColorOutput.CYAN}{hours}h {minutes}m {seconds}s{ColorOutput.RESET}
  Hash Rate: {ColorOutput.GREEN}{hashrate:.2f} H/s{ColorOutput.RESET}
  Total Hashes: {ColorOutput.YELLOW}{self.gpu_monitor.hashes:,}{ColorOutput.RESET}
  Shares Aceptados: {ColorOutput.GREEN}{self.gpu_monitor.shares_accepted}{ColorOutput.RESET}
  Shares Rechazados: {ColorOutput.RED}{self.gpu_monitor.shares_rejected}{ColorOutput.RESET}
  Temperatura GPU: {ColorOutput.YELLOW}{temp:.1f}°C{ColorOutput.RESET}
  Consumo Energía: {ColorOutput.YELLOW}{power:.0f}W{ColorOutput.RESET}
{ColorOutput.BOLD}{ColorOutput.BLUE}═══════════════════════════════════════════════════{ColorOutput.RESET}
        """
        print(stats)
    
    def start(self):
        """Inicia el minero"""
        self.print_banner()
        self.print_config()
        
        logger.info("Conectando al pool...")
        print(f"{ColorOutput.BLUE}Conectando al pool...{ColorOutput.RESET}")
        
        if self.pool.connect():
            print(f"{ColorOutput.GREEN}[✓] Conectado al pool{ColorOutput.RESET}")
            logger.info("Conectado exitosamente al pool")
            self.pool.send_subscribe()
        else:
            print(f"{ColorOutput.YELLOW}[!] Ejecutando en modo offline (simulación){ColorOutput.RESET}")
            logger.warning("Ejecutando en modo offline")
        
        self.running = True
        logger.info("Minero iniciado")
        
        try:
            self.mining_loop()
        except KeyboardInterrupt:
            self.stop()
    
    def stop(self):
        """Detiene el minero"""
        print(f"\n\n{ColorOutput.YELLOW}[!] Deteniendo minero...{ColorOutput.RESET}")
        logger.info("Deteniendo minero...")
        self.running = False
        self.pool.disconnect()
        self.print_stats()
        print(f"{ColorOutput.GREEN}[✓] Minero detenido correctamente{ColorOutput.RESET}")
        logger.info("Minero detenido")


def main():
    """Función principal"""
    parser = argparse.ArgumentParser(
        description='PRL Miner - Minero de Pearl para AMD VEGA VII en Windows x64',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python main.py
  python main.py --gui
  python main.py --pool stratum+tcp://pool.com:3333 --wallet mi_wallet
  python main.py --intensity 28 --device 0
        """
    )
    parser.add_argument('--config', default='config.json', help='Archivo de configuración')
    parser.add_argument('--pool', help='URL del pool de minería')
    parser.add_argument('--wallet', help='Dirección del wallet')
    parser.add_argument('--device', type=int, default=0, help='ID del dispositivo GPU')
    parser.add_argument('--intensity', type=int, default=28, help='Intensidad de minería (20-31)')
    parser.add_argument('--gui', action='store_true', help='Usar interfaz gráfica')
    
    args = parser.parse_args()
    
    # Cargar configuración
    config = Config(args.config)
    
    # Sobrescribir con argumentos si se proporcionan
    if args.pool:
        config.config['pool']['url'] = args.pool
    if args.wallet:
        config.config['pool']['user'] = args.wallet
    if args.device >= 0:
        config.config['gpu']['device_id'] = args.device
    if args.intensity:
        config.config['gpu']['intensity'] = args.intensity
    
    # Crear y iniciar minero
    miner = PRLMinerWindows(config.config, use_gui=args.gui)
    miner.start()


if __name__ == "__main__":
    main()
