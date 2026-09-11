# Release Notes v1.0.0 - Linux Edition

## 📋 Descripción

**PRL Miner v1.0.0 para Linux** es la versión inicial del minero de criptomoneda Pearl optimizado para GPU AMD VEGA VII en sistemas Linux.

### ¿Qué incluye?

- ✅ Motor de minería completamente funcional
- ✅ Soporte para AMD VEGA VII con ROCm
- ✅ Conexión a pools de minería (Stratum protocol)
- ✅ Monitoreo en tiempo real de GPU
- ✅ Estadísticas detalladas de hash rate
- ✅ Gestión de configuración flexible
- ✅ Script de instalación automática
- ✅ Código abierto bajo licencia MIT

## 🎯 Casos de Uso

- Minería individual en Linux
- Minería en pool
- Servidor de minería dedicado
- Laboratorios/investigación

## 📦 Contenido del Release

```
prl-miner-amd-linux-v1.0.0/
├── main.py                    # Programa principal
├── config.json                # Configuración de ejemplo
├── requirements.txt           # Dependencias Python
├── setup.sh                   # Script de instalación
├── README.md                  # Documentación principal
├── LICENSE                    # Licencia MIT
└── .gitignore                 # Archivos a ignorar en git
```

## 🚀 Instalación Rápida

### Requisitos
- Linux (Ubuntu 20.04+ recomendado)
- GPU AMD VEGA VII
- Python 3.8+
- ROCm 5.0+

### Pasos

```bash
# 1. Descargar
wget https://github.com/xxfalaxx/prl-miner-amd/releases/download/v1.0.0-linux/prl-miner-linux-v1.0.0.tar.gz
tar -xzf prl-miner-linux-v1.0.0.tar.gz
cd prl-miner-amd-linux-v1.0.0

# 2. Instalar
chmod +x setup.sh
./setup.sh

# 3. Configurar
nano config.json  # Edita tu wallet address

# 4. Ejecutar
python main.py --wallet TU_WALLET
```

## ⚙️ Configuración Básica

Edita `config.json`:

```json
{
  "pool": {
    "url": "stratum+tcp://pool.prl.com:3333",
    "user": "TU_WALLET_ADDRESS",
    "password": "x"
  },
  "gpu": {
    "device_id": 0,
    "intensity": 28,
    "threads": 1024
  }
}
```

## 🔧 Parámetros de Línea de Comandos

```bash
python main.py --pool stratum+tcp://pool.com:3333 --wallet MI_WALLET --intensity 28 --device 0
```

**Parámetros:**
- `--pool` - URL del pool de minería
- `--wallet` - Dirección de wallet
- `--intensity` - Intensidad (20-31)
- `--device` - ID del dispositivo GPU
- `--config` - Archivo de configuración personalizado

## 📊 Salida de Ejemplo

```
╔════════════════════════════════════════════════════════════════════════════╗
║     PRL MINER - AMD VEGA VII           ║
║     Pearl Cryptocurrency Miner         ║
║     v1.0.0                             ║
╚════════════════════════════════════════════════════════════════════════════╝

Configuración:
  Pool: stratum+tcp://pool.prl.com:3333
  Usuario: wallet_address
  GPU ID: 0
  Intensidad: 28
  Threads: 1024

[✓] Conectado al pool
[✓] Suscrito al pool

[✓ SHARE] Nonce: 1024 | Diff: 5
[✓ SHARE] Nonce: 2048 | Diff: 6

────────────────────────────────────────────────────────────────────────────
Estadísticas de Minería:
  Tiempo: 0h 5m 30s
  Hash Rate: 125.50 H/s
  Total Hashes: 687,750
  Shares Aceptados: 12
  Shares Rechazados: 2
  Temperatura GPU: 65.0°C
  Consumo Energía: 250W
────────────────────────────────────────────────────────────────────────────
```

## 📝 Requisitos del Sistema

### Hardware Mínimo
- GPU: AMD VEGA VII
- RAM: 4GB
- CPU: Dual-core @ 1.5GHz
- Almacenamiento: 500MB libre

### Requisitos de Software
- **OS:** Linux (Ubuntu 20.04+, Debian 11+, Fedora 35+)
- **Python:** 3.8 o superior
- **ROCm:** 5.0 o superior
- **Herramientas:** git, wget, make, gcc

### Instalación de ROCm

```bash
# Ubuntu/Debian
wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install rocm-dkms

# Fedora
sudo dnf install rocm-dkms

# Agregar usuario al grupo video
sudo usermod -a -G video $LOGNAME
```

## 🎨 Características

### Monitoreo en Tiempo Real
- Hash rate (H/s, KH/s, MH/s)
- Temperatura de GPU (°C)
- Consumo de energía (W)
- Shares aceptados/rechazados
- Uptime (Tiempo de ejecución)

### Configuración Flexible
- Pool personalizable
- Parámetros de GPU ajustables
- Diferentes niveles de intensidad
- Logging de operaciones

### Estabilidad
- Reconexión automática al pool
- Manejo de errores robusto
- Validación de configuración
- Logging detallado

## 🐛 Problemas Conocidos

### 1. GPU no detectada
**Solución:**
```bash
rocm-smi  # Verifica que la GPU aparezca
sudo usermod -a -G video $LOGNAME
lo exit y vuelve a entrar
```

### 2. Bajo hash rate
**Solución:** Aumenta `intensity` a 30-31 en config.json

### 3. Temperatura alta
**Solución:** Baja `intensity` a 24-26, aumenta velocidad del ventilador

## 📚 Documentación Adicional

- [README.md](https://github.com/xxfalaxx/prl-miner-amd/blob/main/README.md) - Guía completa
- [GitHub Issues](https://github.com/xxfalaxx/prl-miner-amd/issues) - Reportar problemas
- [GitHub Discussions](https://github.com/xxfalaxx/prl-miner-amd/discussions) - Comunidad

## 🔐 Seguridad

- ✅ No recopila datos personales
- ✅ Sin malware o spyware
- ✅ Código abierto auditable
- ✅ Bajo licencia MIT
- ✅ No modifica archivos del sistema

## 📞 Soporte

- **Issues:** https://github.com/xxfalaxx/prl-miner-amd/issues
- **Discussions:** https://github.com/xxfalaxx/prl-miner-amd/discussions
- **Email:** Abre un issue en el repositorio

## 📄 Licencia

MIT License - Libre para usar, modificar y distribuir

## 🙏 Agradecimientos

- AMD por ROCm
- Comunidad de Pearl
- Contribuidores del proyecto

## 📅 Timeline de Versiones

- **v1.0.0** (11 Sep 2024) - Lanzamiento inicial

---

**Versión:** 1.0.0  
**Fecha de Lanzamiento:** 11 de Septiembre de 2024  
**Plataforma:** Linux x64  
**Estado:** Estable ✅

**[Descargar v1.0.0-linux](https://github.com/xxfalaxx/prl-miner-amd/releases/download/v1.0.0-linux/prl-miner-linux-v1.0.0.tar.gz)**
