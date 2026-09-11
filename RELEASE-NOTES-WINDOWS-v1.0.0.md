# Release Notes v1.0.0 - Windows x64 Edition

## 📋 Descripción

**PRL Miner v1.0.0 para Windows x64** es la versión para Windows del minero de criptomoneda Pearl optimizado para GPU AMD VEGA VII con interfaz gráfica opcional.

### ¿Qué incluye?

- ✅ Motor de minería completamente funcional
- ✅ Soporte para AMD VEGA VII con ROCm/HIP en Windows
- ✅ Interfaz gráfica (GUI) con PyQt5
- ✅ Conexión a pools de minería (Stratum protocol)
- ✅ Monitoreo en tiempo real de GPU
- ✅ Estadísticas detalladas y gráficos
- ✅ Scripts batch (.bat) para ejecución rápida
- ✅ Instalador automático
- ✅ Logging a archivo
- ✅ Gestión de configuración flexible
- ✅ Código abierto bajo licencia MIT

## 🎯 Características Destacadas

### Interfaz Gráfica (GUI)
- 🎨 Diseño moderno y amigable
- 📊 Gráficos en tiempo real del hash rate
- 🌡️ Monitoreo de temperatura y voltaje
- ⚡ Control de parámetros en vivo
- 📈 Estadísticas de sesión
- 💾 Guardado automático de configuración

### Scripts Batch
- `run-gui.bat` - Interfaz gráfica
- `run-cli.bat` - Línea de comandos
- `run-background.bat` - Ejecución en segundo plano
- `setup.bat` - Instalador automático

### Optimizaciones para Windows
- Gestión de prioridad de proceso
- Hardware monitoring nativo
- Integración con Device Manager
- Logging a archivo de sistema
- Minimizar a bandeja del sistema

## 📦 Contenido del Release

```
prl-miner-windows-v1.0.0/
├── main-windows.py            # Programa principal
├── setup-gui.py               # Configurador GUI
├── config-windows.json        # Configuración de ejemplo
├── requirements-windows.txt   # Dependencias Python
├── setup.bat                  # Instalador automático
├── run-gui.bat                # Ejecutar con GUI
├── run-cli.bat                # Ejecutar en CLI
├── run-background.bat         # Ejecutar en background
├── README-WINDOWS.md          # Documentación Windows
├── README.md                  # Documentación principal
├── LICENSE                    # Licencia MIT
└── .gitignore                 # Archivos a ignorar
```

## 🚀 Instalación Rápida

### Requisitos
- **Windows 10/11** x64
- **GPU AMD VEGA VII**
- **Driver AMD Adrenalin 22.12.1** o superior
- **Python 3.9+** (descargable desde python.org)
- **8GB RAM mínimo**

### Instalación de Driver

1. Descarga AMD Adrenalin desde [amd.com](https://www.amd.com/es/support)
2. Instala el driver completo
3. Reinicia tu PC

### Instalación de Python

1. Descarga Python 3.10 desde [python.org](https://www.python.org/downloads/)
2. **IMPORTANTE:** Marca "Add Python to PATH"
3. Instala

### Instalación del Minero

```batch
# 1. Descargar y extraer
Expandir-Archive prl-miner-windows-v1.0.0.zip
cd prl-miner-windows-v1.0.0

# 2. Ejecutar instalador
setup.bat

# 3. Configurar (opcional)
setup-gui.py

# 4. Iniciar minería
run-gui.bat      # Con interfaz gráfica
# O
run-cli.bat      # En línea de comandos
```

## ⚙️ Configuración Básica

Edita `config-windows.json`:

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
    "threads": 1024,
    "core_clock": 1400,
    "memory_clock": 1100
  },
  "windows": {
    "priority": "high",
    "enable_gui": false,
    "minimize_to_tray": true
  }
}
```

## 🎨 Interfaz Gráfica

### Pestañas

**Pool**
- URL del pool
- Wallet address
- Password

**GPU**
- Device ID
- Intensidad (20-31)
- Threads (128-2048)
- Core Clock (MHz)
- Memory Clock (MHz)

**Opciones**
- Hardware monitoring
- Inicio automático
- Minimizar a bandeja

**Monitoring**
- Gráficos en tiempo real
- Estadísticas de shares
- Consumo de energía
- Temperatura

## 🔧 Uso desde Línea de Comandos

```bash
python main-windows.py --pool stratum+tcp://pool.com:3333 --wallet MI_WALLET --intensity 28
```

**Parámetros:**
- `--pool` - URL del pool
- `--wallet` - Dirección de wallet
- `--intensity` - Intensidad (20-31)
- `--device` - ID del dispositivo GPU
- `--config` - Archivo de configuración personalizado
- `--gui` - Habilitar interfaz gráfica

## 📊 Optimizaciones Recomendadas

### Máximo Rendimiento
```json
{
  "intensity": 28,
  "threads": 1024,
  "core_clock": 1500,
  "memory_clock": 1100
}
```
**Rendimiento:** ~120-150 MH/s  
**Consumo:** ~250W  
**Temperatura:** ~70°C

### Balanceado
```json
{
  "intensity": 26,
  "threads": 512,
  "core_clock": 1350,
  "memory_clock": 950
}
```
**Rendimiento:** ~100-120 MH/s  
**Consumo:** ~200W  
**Temperatura:** ~65°C

### Bajo Consumo
```json
{
  "intensity": 24,
  "threads": 256,
  "core_clock": 1200,
  "memory_clock": 800
}
```
**Rendimiento:** ~80-100 MH/s  
**Consumo:** ~150W  
**Temperatura:** ~60°C

## 📈 Salida de Ejemplo

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║     PRL MINER - AMD VEGA VII (Windows x64)                                    ║
║     Pearl Cryptocurrency Miner                                                ║
║     v1.0.0 - Windows Edition                                                  ║
╚═══════════════════════════════════════════════════════════════════════════════╝

Configuración:
  Pool: stratum+tcp://pool.prl.com:3333
  Usuario: wallet_address
  GPU ID: 0
  Intensidad: 28
  Threads: 1024
  Core Clock: 1400 MHz
  Memory Clock: 1100 MHz

[✓] Conectado al pool

[✓ SHARE] Nonce: 1024 | Diff: 5
[✓ SHARE] Nonce: 2048 | Diff: 6

────────────────────────────────────────────────────────────────────────────────
Estadísticas:
  Tiempo: 0h 5m 30s
  Hash Rate: 125.50 H/s
  Total Hashes: 687,750
  Shares Aceptados: 12
  Shares Rechazados: 2
  Temperatura GPU: 65.0°C
  Consumo Energía: 250W
────────────────────────────────────────────────────────────────────────────────
```

## 🐛 Troubleshooting

### GPU no detectada
1. Verifica Driver AMD: `Configuración > Dispositivos > Administrador de dispositivos`
2. Actualiza el driver desde AMD Adrenalin
3. Reinicia tu PC

### Python no reconocido
1. Verifica: `python --version` en CMD
2. Si no funciona, reinstala Python marcando "Add to PATH"
3. Reinicia la terminal

### Bajo hash rate
1. Aumenta `intensity` a 30-31
2. Sube `core_clock` a 1500+ MHz
3. Cierra otros programas que usen GPU

### Temperatura alta
1. Baja `intensity` a 24-26
2. Reduce `core_clock` a 1300 MHz
3. Aumenta velocidad del ventilador en AMD Adrenalin

### Crashes/Freezes
1. Baja `memory_clock` a 950 MHz
2. Reduce `intensity` gradualmente
3. Instala últimos drivers AMD

## 📝 Requisitos del Sistema

### Hardware
- **GPU:** AMD VEGA VII
- **RAM:** 8GB mínimo (16GB recomendado)
- **CPU:** i5/Ryzen 5 o superior
- **Almacenamiento:** 1GB libre
- **Fuente de Poder:** 650W+

### Software
- **Windows:** 10 (build 19041+) o 11
- **Python:** 3.9+
- **Driver AMD:** 22.12.1 o superior
- **Visual C++ Redist:** 2015+
- **.NET Framework:** 4.8+

## 🔐 Seguridad

- ✅ No recopila datos personales
- ✅ Sin malware o spyware verificado
- ✅ Código abierto en GitHub
- ✅ Bajo licencia MIT
- ✅ Usa solo conexiones Stratum estándar
- ✅ No modifica archivos de sistema

## 📊 Monitoreo en Tiempo Real

El minero muestra:
- Hash rate (H/s, MH/s)
- Temperatura de GPU (°C)
- Voltaje de GPU (V)
- Consumo de energía (W)
- Shares aceptados/rechazados
- Velocidad del ventilador (%)
- Uptime
- Earnings estimados

## 📁 Logs

Los logs se guardan en:
```
C:\Users\TU_USUARIO\AppData\Local\PRL-Miner\logs\
```

Para ver logs en tiempo real:
```batch
type prl_miner.log
```

## 🚀 Características Futuras (v1.1.0+)

- [ ] Soporte para múltiples GPUs
- [ ] Dashboard web
- [ ] Inicio automático con Windows
- [ ] Notificaciones de alertas
- [ ] Histórico de ganancias
- [ ] Integración con exchanges
- [ ] Actualizaciones automáticas

## 📞 Soporte

- **Issues:** https://github.com/xxfalaxx/prl-miner-amd/issues
- **Discussions:** https://github.com/xxfalaxx/prl-miner-amd/discussions
- **Documentación:** [README-WINDOWS.md](README-WINDOWS.md)

## 📄 Licencia

MIT License - Libre para usar, modificar y distribuir

## 🙏 Agradecimientos

- AMD por ROCm/HIP
- PyQt5 por la framework GUI
- Comunidad de Pearl

## 📅 Timeline de Versiones

- **v1.0.0** (11 Sep 2024) - Lanzamiento inicial Windows

---

**Versión:** 1.0.0 Windows x64  
**Fecha de Lanzamiento:** 11 de Septiembre de 2024  
**Plataforma:** Windows 10/11 x64  
**Estado:** Estable ✅

**[Descargar v1.0.0-windows](https://github.com/xxfalaxx/prl-miner-amd/releases/download/v1.0.0-windows/prl-miner-windows-v1.0.0.zip)**
