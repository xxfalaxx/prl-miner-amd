@echo off
REM PRL Miner Launcher - Ejecutador del Minero
REM Versación: 1.0.0 (Windows x64)
REM Uso: Doble clic para ejecutar el minero

cd /d "%~dp0"

REM Verificar si Python está disponible
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo [ERROR] Python no está instalado o no está en PATH
    echo.
    echo Soluciones:
    echo 1. Descarga Python desde https://www.python.org/downloads/
    echo 2. Durante la instalación, marca "Add Python to PATH"
    echo 3. Reinicia tu computadora
    echo 4. Vuelve a ejecutar este archivo
    echo.
    pause
    exit /b 1
)

REM Verificar si el archivo de configuración existe
if not exist "config-windows.json" (
    echo.
    echo [ADVERTENCIA] No se encontró config-windows.json
    echo Se usará la configuración por defecto
    echo.
)

REM Mostrar banner
echo.
echo ╔═══════════════════════════════════════════════════════════════════════════════╗
echo ║   PRL MINER - AMD VEGA VII (Windows x64)                  ║
echo ║   Versión: 1.0.0                                            ║
echo ╚═══════════════════════════════════════════════════════════════════════════════╝
echo.
echo Iniciando minero...
echo.

REM Ejecutar el minero
python main-windows.py --config config-windows.json

if errorlevel 1 (
    echo.
    echo [ERROR] Ocurrió un error al ejecutar el minero
    echo Por favor, contacta con soporte
    echo.
    pause
    exit /b 1
)
