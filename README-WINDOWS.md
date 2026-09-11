# PRL Miner AMD VEGA VII - Windows x64

Minero de criptomoneda Pearl (PRL) optimizado para GPU AMD VEGA VII en **Windows x64**.

## 🎯 Características

- ✅ Soporte completo para AMD VEGA VII en Windows x64
- ✅ ROCm/HIP optimizado para Windows
- ✅ Interfaz gráfica (GUI) con PyQt5
- ✅ Conexión a pools de minería
- ✅ Monitoreo en tiempo real
- ✅ Estadísticas detalladas
- ✅ Instalador automático
- ✅ Sin dependencias externas complicadas

## 📋 Requisitos del Sistema

- **Windows 10/11** x64
- **GPU AMD VEGA VII**
- **8GB RAM mínimo** (16GB recomendado)
- **Driver AMD Adrenalin 22.12.1** o superior
- **.NET Framework 4.8** o superior
- **Python 3.9+** (incluido en el instalador)

## 🚀 Instalación Rápida

### Opción 1: Instalador Automático (Recomendado)

1. Descarga `PRL-Miner-Setup.exe` desde [Releases](https://github.com/xxfalaxx/prl-miner-amd/releases)
2. Ejecuta el instalador
3. Sigue los pasos del asistente
4. ¡Listo! El minero estará en `C:\Program Files\PRL-Miner\`

### Opción 2: Instalación Manual

#### Paso 1: Instalar Controladores

1. Descarga el **Driver AMD Adrenalin** desde [amd.com](https://www.amd.com/es/support)
2. Instala el driver completo
3. Reinicia tu PC

#### Paso 2: Instalar Python

1. Descarga Python 3.10 desde [python.org](https://www.python.org/downloads/)
2. **Marca la opción "Add Python to PATH"**
3. Instala

#### Paso 3: Descargar el Minero

```bash
git clone https://github.com/xxfalaxx/prl-miner-amd.git
cd prl-miner-amd
git checkout windows-x64
```

#### Paso 4: Instalar Dependencias

```bash
setup.bat
```

O manualmente:
```bash
pip install -r requirements-windows.txt
```

## ⚙️ Configuración

Edita el archivo `config.json`:

```json
{
  "pool": {
    "url": "stratum+tcp://pool.prl.com:3333",
    "user": "TU_WALLET_ADDRESS_AQUI",
    "password": "x"
  },
  "gpu": {
    "device_id": 0,
    "intensity": 28,
    "threads": 1024,
    "core_clock": 1400,
    "memory_clock": 1100,
    "enable_hw_monitoring": true
  },
  "windows": {
    "priority": "high",
    "enable_gui": true,
    "minimize_to_tray": true,
    "auto_start": false
  }
}
```

### Parámetros Importantes

| Parámetro | Rango | Descripción |
|-----------|-------|-------------|
| `intensity` | 20-31 | Intensidad de trabajo (mayor = más rápido pero más calor) |
| `threads` | 128-2048 | Threads de GPU (depende de tu VEGA VII) |
| `core_clock` | 1000-1600 | Frecuencia del núcleo (MHz) |
| `memory_clock` | 500-1200 | Frecuencia de memoria (MHz) |

## ▶️ Uso

### Interfaz Gráfica (GUI)

```bash
python main.py --gui
```

O simplemente ejecuta `run-gui.bat`

### Línea de Comandos (CLI)

```bash
python main.py
```

### Con Parámetros Personalizados

```bash
python main.py --pool stratum+tcp://pool.ejemplo.com:3333 --wallet TU_WALLET --intensity 28 --device 0
```

### Scripts Rápidos

**Ejecutar GUI:**
```bash
run-gui.bat
```

**Ejecutar CLI:**
```bash
run-cli.bat
```

**Ejecutar en segundo plano:**
```bash
run-background.bat
```

## 📊 Interfaz Gráfica

La GUI incluye:

- 📈 Gráficos en tiempo real de hash rate
- 🌡️ Monitoreo de temperatura y voltaje
- ⚡ Consumo de energía
- 💰 Estadísticas de shares
- 🎚️ Controles deslizantes para ajustar intensidad
- 🔔 Notificaciones del sistema
- 💾 Historial de sesiones

## 🔧 Optimización para VEGA VII

### Configuración Recomendada para máximo rendimiento:

```json
{
  "gpu": {
    "intensity": 28,
    "threads": 1024,
    "core_clock": 1500,
    "memory_clock": 1100,
    "power_limit": 250
  }
}
```

### Configuración Balanceada (rendimiento vs consumo):

```json
{
  "gpu": {
    "intensity": 26,
    "threads": 512,
    "core_clock": 1350,
    "memory_clock": 950,
    "power_limit": 200
  }
}
```

## 📞 Troubleshooting

### El minero no detecta la GPU

1. Verifica que el driver AMD esté instalado: `radeon-settings.exe`
2. En Device Manager, asegúrate que la VEGA VII aparezca sin errores
3. Reinicia tu PC
4. Actualiza el driver a la versión más reciente

### Bajo hash rate

1. Aumenta `intensity` en config.json (máximo 31)
2. Aumenta `threads` (prueba 1024 o 2048)
3. Sube `core_clock` y `memory_clock`
4. Asegúrate de que no hay otros programas usando GPU

### Temperatura muy alta

1. Baja `intensity` a 24-26
2. Reduce `core_clock` a 1300 MHz
3. Aumenta la velocidad del ventilador (AMD Adrenalin → Performance → Fan Control)
4. Limpia el polvo de tu GPU

### El programa se cierra al iniciar

1. Ejecuta `python main.py` en terminal para ver el error
2. Verifica que Python esté en PATH: `python --version`
3. Reinstala las dependencias: `pip install -r requirements-windows.txt --force-reinstall`

## 📈 Monitoreo

El minero muestra en tiempo real:

- **Hash Rate** (MH/s o H/s)
- **Temperatura de GPU** (°C)
- **Voltaje de GPU** (V)
- **Consumo de Energía** (W)
- **Shares Aceptados/Rechazados**
- **Velocidad del Ventilador** (%)
- **Uptime** (Tiempo de ejecución)
- **Earnings Estimados** (USD/día)

## 🔐 Seguridad

- El minero **NO recopila** datos personales
- **NO contiene** malware o spyware
- **NO modifica** archivos del sistema
- **Código abierto** - audita el código en GitHub

## 📝 Logs

Los logs se guardan en:
```
C:\Users\TU_USUARIO\AppData\Local\PRL-Miner\logs\
```

## 🤝 Soporte

- Abre un [Issue](https://github.com/xxfalaxx/prl-miner-amd/issues)
- Mira las [Discusiones](https://github.com/xxfalaxx/prl-miner-amd/discussions)

## 📄 Licencia

MIT License - [Ver LICENSE](LICENSE)

## ⚠️ Disclaimer

Este software se proporciona "tal cual". El autor no se responsabiliza por:
- Daños en el hardware
- Pérdidas económicas
- Incompatibilidades con otros programas

Usa bajo tu propio riesgo.

---

**Versión:** 1.0.0 (Windows x64)  
**Última actualización:** 2024  
**Compatible:** Windows 10/11 x64 + AMD VEGA VII
