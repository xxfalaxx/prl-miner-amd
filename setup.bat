@echo off
REM Instalador automático de dependencias para PRL Miner - Windows

echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║   PRL Miner AMD VEGA VII - Instalador de Dependencias     ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no está instalado o no está en PATH
    echo.
    echo Solución:
    echo 1. Descarga Python desde https://www.python.org/downloads/
    echo 2. Marca la opción "Add Python to PATH" durante la instalación
    echo 3. Reinicia esta terminal
    pause
    exit /b 1
)

echo [1/3] Actualizando pip...
python -m pip install --upgrade pip setuptools wheel

echo.
echo [2/3] Instalando dependencias...
pip install -r requirements-windows.txt

echo.
echo [3/3] Creando accesos directos...

REM Crear accesos directos para scripts
if not exist "shortcuts" mkdir shortcuts

echo @echo off > shortcuts\run-gui.bat
echo python "%CD%\main-windows.py" --gui >> shortcuts\run-gui.bat

echo @echo off > shortcuts\run-cli.bat
echo python "%CD%\main-windows.py" >> shortcuts\run-cli.bat

echo @echo off > shortcuts\run-background.bat
echo start /min /B pythonw "%CD%\main-windows.py" >> shortcuts\run-background.bat

echo.
echo ═══════════════════════════════════════════════════════════
echo [✓] Instalación completada!
echo ═══════════════════════════════════════════════════════════
echo.
echo Próximos pasos:
echo.
echo  1. Edita config-windows.json con tu wallet address
echo  2. Ejecuta: run-gui.bat (Interfaz gráfica)
echo     O: run-cli.bat (Línea de comandos)
echo  3. Ajusta la intensidad si es necesario
echo.
echo Archivos creados en: shortcuts\
echo.
pause
