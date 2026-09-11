#!/usr/bin/env python3
"""
Instalador gráfico para PRL Miner en Windows
"""

import sys
import os
import subprocess
from pathlib import Path

try:
    from PyQt5.QtWidgets import (
        QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
        QPushButton, QLabel, QLineEdit, QSpinBox, QCheckBox, QComboBox,
        QFileDialog, QMessageBox, QTabWidget, QGroupBox, QGridLayout
    )
    from PyQt5.QtCore import Qt, QThread, pyqtSignal
    from PyQt5.QtGui import QFont, QIcon, QPixmap
    PYQT5_AVAILABLE = True
except ImportError:
    PYQT5_AVAILABLE = False
    print("Error: PyQt5 no está instalado.")
    print("Ejecuta: pip install PyQt5")
    sys.exit(1)

import json


class MinerThread(QThread):
    """Thread para ejecutar el minero sin bloquear la GUI"""
    output_signal = pyqtSignal(str)
    
    def __init__(self, config_file):
        super().__init__()
        self.config_file = config_file
        self.running = True
    
    def run(self):
        """Ejecuta el minero"""
        try:
            subprocess.run([sys.executable, 'main-windows.py', '--config', self.config_file])
        except Exception as e:
            self.output_signal.emit(f"Error: {e}")
    
    def stop(self):
        """Detiene el minero"""
        self.running = False


class MinerConfigGUI(QMainWindow):
    """Interfaz gráfica para configurar y ejecutar PRL Miner"""
    
    def __init__(self):
        super().__init__()
        self.config_file = 'config-windows.json'
        self.miner_thread = None
        self.init_ui()
        self.load_config()
    
    def init_ui(self):
        """Inicializa la interfaz gráfica"""
        self.setWindowTitle('PRL Miner Setup - AMD VEGA VII')
        self.setGeometry(100, 100, 600, 700)
        
        # Widget principal
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        
        # Título
        title = QLabel('PRL Miner para AMD VEGA VII - Windows x64')
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        main_layout.addWidget(title)
        
        # Tabs
        tabs = QTabWidget()
        
        # Tab 1: Pool
        pool_widget = QWidget()
        pool_layout = QGridLayout(pool_widget)
        
        pool_layout.addWidget(QLabel('URL del Pool:'), 0, 0)
        self.pool_url = QLineEdit()
        pool_layout.addWidget(self.pool_url, 0, 1)
        
        pool_layout.addWidget(QLabel('Wallet Address:'), 1, 0)
        self.wallet = QLineEdit()
        pool_layout.addWidget(self.wallet, 1, 1)
        
        pool_layout.addWidget(QLabel('Password:'), 2, 0)
        self.password = QLineEdit()
        self.password.setText('x')
        pool_layout.addWidget(self.password, 2, 1)
        
        tabs.addTab(pool_widget, 'Pool')
        
        # Tab 2: GPU
        gpu_widget = QWidget()
        gpu_layout = QGridLayout(gpu_widget)
        
        gpu_layout.addWidget(QLabel('Device ID:'), 0, 0)
        self.device_id = QSpinBox()
        self.device_id.setMaximum(8)
        gpu_layout.addWidget(self.device_id, 0, 1)
        
        gpu_layout.addWidget(QLabel('Intensidad:'), 1, 0)
        self.intensity = QSpinBox()
        self.intensity.setMinimum(20)
        self.intensity.setMaximum(31)
        self.intensity.setValue(28)
        gpu_layout.addWidget(self.intensity, 1, 1)
        
        gpu_layout.addWidget(QLabel('Threads:'), 2, 0)
        self.threads = QSpinBox()
        self.threads.setMinimum(128)
        self.threads.setMaximum(2048)
        self.threads.setSingleStep(128)
        self.threads.setValue(1024)
        gpu_layout.addWidget(self.threads, 2, 1)
        
        gpu_layout.addWidget(QLabel('Core Clock (MHz):'), 3, 0)
        self.core_clock = QSpinBox()
        self.core_clock.setMinimum(800)
        self.core_clock.setMaximum(1800)
        self.core_clock.setValue(1400)
        gpu_layout.addWidget(self.core_clock, 3, 1)
        
        gpu_layout.addWidget(QLabel('Memory Clock (MHz):'), 4, 0)
        self.mem_clock = QSpinBox()
        self.mem_clock.setMinimum(500)
        self.mem_clock.setMaximum(1200)
        self.mem_clock.setValue(1100)
        gpu_layout.addWidget(self.mem_clock, 4, 1)
        
        tabs.addTab(gpu_widget, 'GPU')
        
        # Tab 3: Opciones
        options_widget = QWidget()
        options_layout = QVBoxLayout(options_widget)
        
        self.hw_monitoring = QCheckBox('Habilitar monitoreo de hardware')
        self.hw_monitoring.setChecked(True)
        options_layout.addWidget(self.hw_monitoring)
        
        self.auto_start = QCheckBox('Iniciar automáticamente')
        options_layout.addWidget(self.auto_start)
        
        self.minimize_tray = QCheckBox('Minimizar a bandeja de sistema')
        self.minimize_tray.setChecked(True)
        options_layout.addWidget(self.minimize_tray)
        
        tabs.addTab(options_widget, 'Opciones')
        
        main_layout.addWidget(tabs)
        
        # Botones
        button_layout = QHBoxLayout()
        
        save_btn = QPushButton('Guardar Configuración')
        save_btn.clicked.connect(self.save_config)
        button_layout.addWidget(save_btn)
        
        start_btn = QPushButton('Iniciar Minería')
        start_btn.clicked.connect(self.start_mining)
        button_layout.addWidget(start_btn)
        
        main_layout.addLayout(button_layout)
        
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
    
    def load_config(self):
        """Carga la configuración desde archivo"""
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            self.pool_url.setText(config['pool']['url'])
            self.wallet.setText(config['pool']['user'])
            self.device_id.setValue(config['gpu']['device_id'])
            self.intensity.setValue(config['gpu']['intensity'])
            self.threads.setValue(config['gpu']['threads'])
            self.core_clock.setValue(config['gpu']['core_clock'])
            self.mem_clock.setValue(config['gpu']['memory_clock'])
            self.hw_monitoring.setChecked(config['gpu']['enable_hw_monitoring'])
        except Exception as e:
            QMessageBox.warning(self, 'Error', f'Error cargando config: {e}')
    
    def save_config(self):
        """Guarda la configuración"""
        config = {
            "pool": {
                "url": self.pool_url.text(),
                "user": self.wallet.text(),
                "password": self.password.text()
            },
            "gpu": {
                "device_id": self.device_id.value(),
                "intensity": self.intensity.value(),
                "threads": self.threads.value(),
                "core_clock": self.core_clock.value(),
                "memory_clock": self.mem_clock.value(),
                "power_limit": 250,
                "enable_hw_monitoring": self.hw_monitoring.isChecked()
            },
            "windows": {
                "priority": "high",
                "enable_gui": False,
                "minimize_to_tray": self.minimize_tray.isChecked(),
                "auto_start": self.auto_start.isChecked()
            },
            "monitoring": {
                "enabled": True,
                "interval": 5,
                "verbose": True
            }
        }
        
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            QMessageBox.information(self, 'Éxito', 'Configuración guardada correctamente')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error guardando config: {e}')
    
    def start_mining(self):
        """Inicia la minería"""
        self.save_config()
        QMessageBox.information(self, 'Iniciando', 'El minero se iniciará en una nueva ventana')
        
        try:
            subprocess.Popen([sys.executable, 'main-windows.py', '--config', self.config_file])
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error iniciando minero: {e}')


def main():
    app = QApplication(sys.argv)
    window = MinerConfigGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
