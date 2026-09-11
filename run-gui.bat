@echo off
REM Script rápido para ejecutar PRL Miner con GUI

cd /d "%~dp0"

echo Iniciando PRL Miner con interfaz gráfica...
echo.

python main-windows.py --gui --config config-windows.json

pause
