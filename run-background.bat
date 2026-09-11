@echo off
REM Script para ejecutar PRL Miner en segundo plano sin ventana

cd /d "%~dp0"

start /min /B pythonw main-windows.py --config config-windows.json

echo PRL Miner iniciado en segundo plano
echo Cierra esta ventana para continuar

pause
