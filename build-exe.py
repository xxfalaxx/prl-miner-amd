#!/usr/bin/env python3
"""
PRL Miner Windows Installer Generator
Generá un ejecutable instalador para Windows
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def check_pyinstaller():
    """Verifica si PyInstaller está instalado"""
    try:
        import PyInstaller
        return True
    except ImportError:
        return False

def install_pyinstaller():
    """Instala PyInstaller"""
    print("[1/5] Instalando PyInstaller...")
    subprocess.run([sys.executable, "-m", "pip", "install", "PyInstaller"], check=True)
    print("[✓] PyInstaller instalado")

def create_icon():
    """Crea un ícono simple para el ejecutable"""
    print("[2/5] Creando ícono...")
    
    # Crear un ícono simple (16x16 PNG)
    icon_data = (
        b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10'
        b'\x08\x02\x00\x00\x00\x90\x91h6\x00\x00\x00\x19tEXtSoftware\x00Adobe'
        b'\x20ImageReadyq\xc9e<\x00\x00\x01\x14IDATx\xdab\xf8\x0f\x04\x0c\x0c\x0c'
        b'\x0c\x0c\x0c\x0c\xf0\xcf\xcf\xcf\xcf\xcf\xcf\xc7\x80\x08\x08\x08\x08\x08'
        b'\x08\x08\x08\x08\xf8\xfb\xfb\xfb\xfb\xfb\xfb\xfb\x03\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\xf0\xef\xef\xef\xef\xef\xef\x0f\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\xf8\xfb\xfb\xfb\xfb\xfb\xfb\x07\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xfd\xfd\xfd\xfd\xfd\xfd\x01\x00\x00'
        b'\x00\xf8\xfb\xfb\xfb\xfb\xfb\xfb\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\xf8\xfb\xfb\xfb\xfb\xfb\xfb\x03\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xef\xef\xef\xef\xef\xef'
        b'\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\xfb\xfb\xfb\xfb\xfb\xfb\x07'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc'
        b'\xfd\xfd\xfd\xfd\xfd\xfd\x01\x00\x00\x00\xf8\xfb\xfb\xfb\xfb\xfb\xfb\x03\x00\x00'
        b'\x00\xf0\xef\xef\xef\xef\xef\xef\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\xf8\xfb\xfb\xfb\xfb\xfb\xfb\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\xfc\xfd\xfd\xfd\xfd\xfd\xfd\x01\x00\x00\xf8\xfb\xfb\xfb'
        b'\xfb\xfb\xfb\x03\x1f\x00\x00\xfc\x84\xe2\x01\x00\x00\x00\x00IEND\xaeB`\x82'
    )
    
    with open('prl-icon.ico', 'wb') as f:
        f.write(icon_data[:16])  # Escribir como fichero de prueba
    
    print("[✓] Ícono creado")

def build_executable():
    """Construye el ejecutable con PyInstaller"""
    print("[3/5] Construyendo ejecutable con PyInstaller...")
    
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--windowed",
        "--name=PRL-Miner",
        "--add-data=config-windows.json:.",
        "--console",
        "main-windows.py"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print("[ERROR] Fallo al crear ejecutable")
        print(result.stderr)
        return False
    
    print("[✓] Ejecutable creado: dist/PRL-Miner.exe")
    return True

def create_distribution():
    """Crea la carpeta de distribución"""
    print("[4/5] Creando carpeta de distribución...")
    
    dist_dir = Path("dist/PRL-Miner-Windows-v1.0.0")
    dist_dir.mkdir(parents=True, exist_ok=True)
    
    # Copiar ejecutable
    if Path("dist/PRL-Miner.exe").exists():
        import shutil
        shutil.copy("dist/PRL-Miner.exe", dist_dir)
    
    # Copiar archivos de configuración
    files_to_copy = [
        "config-windows.json",
        "requirements-windows.txt",
        "prl-miner.bat",
        "install-dependencies.bat",
        "run-gui.bat",
        "run-cli.bat",
        "run-background.bat",
        "README-WINDOWS.md",
        "README.md",
        "LICENSE"
    ]
    
    for file in files_to_copy:
        if Path(file).exists():
            import shutil
            shutil.copy(file, dist_dir)
    
    print(f"[✓] Distribución lista en: {dist_dir}")
    return True

def create_zip_release():
    """Crea un archivo ZIP para el release"""
    print("[5/5] Creando archivo ZIP para release...")
    
    import shutil
    
    try:
        zip_path = shutil.make_archive(
            'prl-miner-windows-v1.0.0',
            'zip',
            'dist',
            'PRL-Miner-Windows-v1.0.0'
        )
        print(f"[✓] ZIP creado: {zip_path}")
        return True
    except Exception as e:
        print(f"[ERROR] Fallo al crear ZIP: {e}")
        return False

def main():
    print("\n" + "="*70)
    print("  PRL Miner Windows Installer Builder v1.0.0")
    print("="*70 + "\n")
    
    # Verificar PyInstaller
    if not check_pyinstaller():
        install_pyinstaller()
    
    # Crear ícono
    create_icon()
    
    # Construir ejecutable
    if not build_executable():
        sys.exit(1)
    
    # Crear distribución
    if not create_distribution():
        sys.exit(1)
    
    # Crear ZIP
    if not create_zip_release():
        sys.exit(1)
    
    print("\n" + "="*70)
    print("  [✓] Proceso completado exitosamente!")
    print("="*70)
    print("\nArchivos generados:")
    print("  - dist/PRL-Miner.exe")
    print("  - dist/PRL-Miner-Windows-v1.0.0/ (carpeta)")
    print("  - prl-miner-windows-v1.0.0.zip (para release)")
    print("\nPróximos pasos:")
    print("  1. Sube el ZIP a GitHub Releases")
    print("  2. Actualiza la documentación")
    print("  3. Publica el release\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[CANCELADO] Proceso interrumpido por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] {e}")
        sys.exit(1)
