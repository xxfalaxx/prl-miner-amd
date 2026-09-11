@echo off
REM PRL Miner - Instalador Ejecutable para Windows x64
REM Versión: 1.0.0
REM Este script crea un instalador .exe usando PyInstaller

echo.
echo ╔═══════════════════════════════════════════════════════════════════════════════╗
echo ║   PRL Miner - Generador de Ejecutable (PyInstaller)         ║
echo ╚═══════════════════════════════════════════════════════════════════════════════╝
echo.

REM Verificar si PyInstaller está instalado
python -m pip list | findstr PyInstaller >nul 2>&1
if errorlevel 1 (
    echo [1/4] Instalando PyInstaller...
    python -m pip install PyInstaller
) else (
    echo [1/4] PyInstaller ya está instalado
)

echo.
echo [2/4] Limpiando directorios previos...
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build
if exist __pycache__ rmdir /s /q __pycache__

echo.
echo [3/4] Generando ejecutable...
pyinstaller --onefile --windowed --icon=prl-icon.ico --add-data "config-windows.json:." main-windows.py -n "PRL-Miner"

if errorlevel 1 (
    echo.
    echo [ERROR] Fallo al crear el ejecutable
    pause
    exit /b 1
)

echo.
echo [4/4] Creando carpeta de distribución...
if not exist "dist\PRL-Miner-v1.0.0" mkdir "dist\PRL-Miner-v1.0.0"

REM Copiar archivos necesarios
copy dist\PRL-Miner.exe "dist\PRL-Miner-v1.0.0\"
copy config-windows.json "dist\PRL-Miner-v1.0.0\"
copy requirements-windows.txt "dist\PRL-Miner-v1.0.0\"
copy setup.bat "dist\PRL-Miner-v1.0.0\"
copy run-gui.bat "dist\PRL-Miner-v1.0.0\"
copy run-cli.bat "dist\PRL-Miner-v1.0.0\"
copy run-background.bat "dist\PRL-Miner-v1.0.0\"
copy README-WINDOWS.md "dist\PRL-Miner-v1.0.0\"
copy README.md "dist\PRL-Miner-v1.0.0\"
copy LICENSE "dist\PRL-Miner-v1.0.0\"

echo.
echo ═══════════════════════════════════════════════════════════════════════════════
echo [✓] Éxito! Ejecutable creado
echo ═══════════════════════════════════════════════════════════════════════════════
echo.
echo Ubicación: dist\PRL-Miner-v1.0.0\
echo Archivos generados:
echo   - PRL-Miner.exe
echo   - config-windows.json
echo   - requirements-windows.txt
echo   - setup.bat
echo   - run-gui.bat
echo   - run-cli.bat
echo   - run-background.bat
echo   - README-WINDOWS.md
echo   - README.md
echo   - LICENSE
echo.
echo Para usar:
echo   1. Copia la carpeta PRL-Miner-v1.0.0 a tu PC
echo   2. Ejecuta: PRL-Miner.exe
echo   3. O ejecuta: run-gui.bat o run-cli.bat
echo.
pause
