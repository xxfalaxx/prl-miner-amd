#!/bin/bash

# Script de instalación para PRL Miner AMD VEGA VII

echo "╔════════════════════════════════════════╗"
echo "║   PRL Miner AMD VEGA VII Setup         ║"
echo "╚════════════════════════════════════════╝"

# Verificar si es Linux
if [[ "$OSTYPE" != "linux-gnu"* ]]; then
    echo "[ERROR] Este script solo funciona en Linux"
    exit 1
fi

echo "[1/4] Actualizando sistema..."
sudo apt-get update && sudo apt-get upgrade -y

echo "[2/4] Instalando ROCm..."
wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
sudo apt-get install -y rocm-dkms rocm-libs rocm-dev

echo "[3/4] Agregando usuario al grupo video..."
sudo usermod -a -G video $LOGNAME

echo "[4/4] Instalando dependencias Python..."
pip install -r requirements.txt

echo ""
echo "[✓] Instalación completada!"
echo ""
echo "Próximos pasos:"
echo "  1. Edita config.json con tu dirección de wallet"
echo "  2. Ejecuta: python main.py"
echo ""
echo "Para cambiar el pool, usa:"
echo "  python main.py --pool stratum+tcp://pool.com:3333 --wallet TU_WALLET"
