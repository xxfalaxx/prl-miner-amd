@echo off
REM PRL Miner Setup - Instalador rápido para Windows
REM Versión: 1.0.0

echo.
echo ╔═══════════════════════════════════════════════════════════════════════════════╗
echo ║   PRL Miner - Instalador de Dependencias                  ║
echo ╚═══════════════════════════════════════════════════════════════════════════════╝
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no está instalado o no está en PATH
    echo.
    echo Soluciones:
    echo 1. Descarga Python 3.10+ desde https://www.python.org/downloads/
    echo 2. Durante la instalación, marca "Add Python to PATH"
    echo 3. Reinicia tu computadora
    echo 4. Vuelve a ejecutar este archivo
    echo.
    pause
    exit /b 1
)

echo [1/3] Actualizando pip...
python -m pip install --upgrade pip setuptools wheel

echo.
echo [2/3] Instalando dependencias...
if exist "requirements-windows.txt" (
    pip install -r requirements-windows.txt
) else (
    echo [ADVERTENCIA] No se encontró requirements-windows.txt
    echo Instala manualmente: pip install PyQt5 requests psutil
)

echo.
echo [3/3] Verificando instalación...
python -c "import PyQt5; print('[OK] PyQt5 instalado')" 2>nul
if errorlevel 1 (
    echo [ADVERTENCIA] PyQt5 no se pudo instalar completamente
    echo El minero seguirá funcionando en modo CLI
)

echo.
echo ═══════════════════════════════════════════════════════════════════════════════
echo [✓] Instalación completada!
echo ═══════════════════════════════════════════════════════════════════════════════
echo.
echo Próximos pasos:
echo.
echo 1. Edita config-windows.json con tu wallet address
echo 2. Ejecuta prl-miner.bat para iniciar la minería
echo.
pause
