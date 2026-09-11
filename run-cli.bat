@echo off
REM Script rápido para ejecutar PRL Miner en línea de comandos

cd /d "%~dp0"

echo Iniciando PRL Miner...
echo.

python main-windows.py --config config-windows.json

pause
