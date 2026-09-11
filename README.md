# PRL Miner AMD VEGA VII

Minero de criptomoneda Pearl (PRL) optimizado para GPU AMD VEGA VII.

## Características

- ✅ Soporte completo para AMD VEGA VII
- ✅ Conexión a pools de minería
- ✅ Monitoreo en tiempo real
- ✅ Configuración flexible
- ✅ Estadísticas de rendimiento
- ✅ Compatible con ROCm

## Requisitos

- GPU AMD VEGA VII
- AMD ROCm 5.0+
- Python 3.8+
- pip (gestor de paquetes Python)

## Instalación

### 1. Instalar ROCm

```bash
# En Linux (Ubuntu/Debian)
wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install rocm-dkms

# Agregar usuario al grupo video
sudo usermod -a -G video $LOGNAME
```

### 2. Clonar repositorio

```bash
git clone https://github.com/xxfalaxx/prl-miner-amd.git
cd prl-miner-amd
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Configuración

Edita el archivo `config.json`:

```json
{
  "pool": {
    "url": "stratum+tcp://pool.example.com:3333",
    "user": "tu_wallet_address",
    "password": "x"
  },
  "gpu": {
    "device_id": 0,
    "intensity": 28,
    "threads": 1024
  },
  "monitoring": {
    "enabled": true,
    "interval": 5
  }
}
```

## Uso

```bash
python main.py
```

## Parámetros

- `--config` - Archivo de configuración (default: config.json)
- `--pool` - URL del pool de minería
- `--wallet` - Dirección del wallet
- `--device` - ID del dispositivo GPU (0, 1, 2...)
- `--intensity` - Intensidad de minería (20-31)

## Ejemplo

```bash
python main.py --pool stratum+tcp://pool.prl.com:3333 --wallet TU_WALLET --intensity 28
```

## Monitoreo

El minero muestra en tiempo real:
- Hash rate (MH/s)
- Temperatura de GPU
- Consumo de energía
- Shares aceptadas/rechazadas
- Tiempo de conexión

## Licencia

MIT License - Ver LICENSE para más detalles

## Soporte

Para reportar problemas, abre un issue en el repositorio.
