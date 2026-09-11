# 📋 Guía para Crear Releases en GitHub

Esta guía te explica paso a paso cómo crear releases oficiales para PRL Miner en GitHub.

## 📌 Prerrequisitos

- Acceso de administrador al repositorio
- Git instalado localmente
- Repositorio clonado en tu PC

## 🔤 Pasos para Crear un Release

### Opción 1: Desde GitHub Web (Recomendado)

#### Paso 1: Navega a Releases
1. Ve a: https://github.com/xxfalaxx/prl-miner-amd
2. Haz clic en **"Releases"** en la barra lateral derecha
3. Haz clic en **"Create a new release"**

#### Paso 2: Crear Release de Linux v1.0.0

**Información:**
- **Tag version:** `v1.0.0-linux`
- **Target:** `main` (rama)
- **Release title:** `PRL Miner v1.0.0 - Linux Edition`
- **Description:** Copia el contenido de `RELEASE-NOTES-LINUX-v1.0.0.md`

**Pasos:**
1. En "Tag version", escribe: `v1.0.0-linux`
2. Selecciona rama: `main`
3. En "Release title", escribe: `PRL Miner v1.0.0 - Linux Edition`
4. En "Describe this release", copia el contenido del archivo `RELEASE-NOTES-LINUX-v1.0.0.md`
5. Opcionalmente marca "This is a pre-release" si es versión beta
6. Haz clic en **"Publish release"**

#### Paso 3: Agregar Archivo de Descarga (Linux)

**Preparar el archivo:**

```bash
# En tu PC, en la carpeta del repositorio
mkdir -p releases

# Crear archivo comprimido
tar -czf prl-miner-linux-v1.0.0.tar.gz \
  main.py config.json requirements.txt setup.sh README.md LICENSE .gitignore

# Mover a carpeta de releases
mv prl-miner-linux-v1.0.0.tar.gz releases/
```

**Subir el archivo:**
1. En el release recién creado, haz clic en **"Edit"**
2. En la sección "Attachments", arrastra y suelta o selecciona:
   - `prl-miner-linux-v1.0.0.tar.gz`
3. Haz clic en **"Update release"**

#### Paso 4: Crear Release de Windows v1.0.0

**Información:**
- **Tag version:** `v1.0.0-windows`
- **Target:** `windows-x64` (rama)
- **Release title:** `PRL Miner v1.0.0 - Windows x64 Edition`
- **Description:** Copia el contenido de `RELEASE-NOTES-WINDOWS-v1.0.0.md`

**Pasos:**
1. Vuelve a la página de Releases
2. Haz clic en **"Create a new release"**
3. En "Tag version", escribe: `v1.0.0-windows`
4. Selecciona rama: `windows-x64`
5. En "Release title", escribe: `PRL Miner v1.0.0 - Windows x64 Edition`
6. En "Describe this release", copia el contenido del archivo `RELEASE-NOTES-WINDOWS-v1.0.0.md`
7. Haz clic en **"Publish release"**

#### Paso 5: Agregar Archivo de Descarga (Windows)

**Preparar el archivo:**

```bash
# En tu PC, en la carpeta del repositorio en rama windows-x64
cd releases

# Crear archivo comprimido (en Windows o con 7-Zip)
# Selecciona estos archivos:
# - main-windows.py
# - setup-gui.py
# - config-windows.json
# - requirements-windows.txt
# - setup.bat
# - run-gui.bat
# - run-cli.bat
# - run-background.bat
# - README-WINDOWS.md
# - README.md
# - LICENSE
# - .gitignore

# Crear ZIP
# En Windows: Click derecho > Enviar a > Carpeta comprimida
# Resultado: prl-miner-windows-v1.0.0.zip
```

**Subir el archivo:**
1. En el release de Windows, haz clic en **"Edit"**
2. Arrastra y suelta o selecciona:
   - `prl-miner-windows-v1.0.0.zip`
3. Haz clic en **"Update release"**

### Opción 2: Desde Terminal (Usando Git)

#### Para Linux v1.0.0

```bash
# 1. Estar en rama main
git checkout main
git pull origin main

# 2. Crear etiqueta
git tag -a v1.0.0-linux -m "PRL Miner v1.0.0 - Linux Edition"

# 3. Subir etiqueta a GitHub
git push origin v1.0.0-linux

# 4. En GitHub, ve a Releases y completa la información
```

#### Para Windows v1.0.0

```bash
# 1. Estar en rama windows-x64
git checkout windows-x64
git pull origin windows-x64

# 2. Crear etiqueta
git tag -a v1.0.0-windows -m "PRL Miner v1.0.0 - Windows x64 Edition"

# 3. Subir etiqueta a GitHub
git push origin v1.0.0-windows

# 4. En GitHub, ve a Releases y completa la información
```

## 📦 Preparación de Archivos de Descarga

### Linux

```bash
# Desde la rama main
cd /ruta/del/repositorio

# Crear directorio temporal
mkdir -p build/prl-miner-linux-v1.0.0
cd build/prl-miner-linux-v1.0.0

# Copiar archivos
cp ../../main.py .
cp ../../config.json .
cp ../../requirements.txt .
cp ../../setup.sh .
cp ../../README.md .
cp ../../LICENSE .
cp ../../.gitignore .

# Crear tarball
cd ..
tar -czf prl-miner-linux-v1.0.0.tar.gz prl-miner-linux-v1.0.0/

# Resultado: build/prl-miner-linux-v1.0.0.tar.gz
```

### Windows

```bash
# Desde la rama windows-x64
cd /ruta/del/repositorio

# Crear directorio temporal
mkdir -p build\prl-miner-windows-v1.0.0
cd build\prl-miner-windows-v1.0.0

# Copiar archivos
copy ...\main-windows.py .
copy ...\setup-gui.py .
copy ...\config-windows.json .
copy ...\requirements-windows.txt .
copy ...\setup.bat .
copy ...\run-gui.bat .
copy ...\run-cli.bat .
copy ...\run-background.bat .
copy ...\README-WINDOWS.md .
copy ...\README.md .
copy ...\LICENSE .
copy ...\gitignore .gitignore

# Crear ZIP (usar 7-Zip, WinRAR o Windows Explorer)
# Resultado: build\prl-miner-windows-v1.0.0.zip
```

## ✅ Checklist Final

### Antes de Crear el Release de Linux

- [ ] Rama `main` está actualizada
- [ ] Archivo `RELEASE-NOTES-LINUX-v1.0.0.md` existe
- [ ] Archivo `prl-miner-linux-v1.0.0.tar.gz` está preparado
- [ ] El README.md del repositorio está completo
- [ ] Todos los archivos Python funcionan sin errores
- [ ] requirements.txt está actualizado

### Antes de Crear el Release de Windows

- [ ] Rama `windows-x64` está actualizada
- [ ] Archivo `RELEASE-NOTES-WINDOWS-v1.0.0.md` existe
- [ ] Archivo `prl-miner-windows-v1.0.0.zip` está preparado
- [ ] Archivos batch (.bat) están incluidos
- [ ] setup-gui.py está funcional
- [ ] requirements-windows.txt está actualizado
- [ ] README-WINDOWS.md está completo

## 🔗 URLs de Descarga

Una vez publicados los releases, los URLs serán:

**Linux v1.0.0:**
```
https://github.com/xxfalaxx/prl-miner-amd/releases/download/v1.0.0-linux/prl-miner-linux-v1.0.0.tar.gz
```

**Windows v1.0.0:**
```
https://github.com/xxfalaxx/prl-miner-amd/releases/download/v1.0.0-windows/prl-miner-windows-v1.0.0.zip
```

## 📝 Ejemplo de Descripción del Release

```markdown
# PRL Miner v1.0.0 - Linux Edition

Primer lanzamiento oficial del minero de Pearl para AMD VEGA VII en Linux.

## Características

- ✅ Soporte completo para AMD VEGA VII
- ✅ Conexión a pools de minería
- ✅ Monitoreo en tiempo real
- ✅ Configuración flexible
- ✅ Código abierto bajo MIT License

## Instalación Rápida

```bash
tar -xzf prl-miner-linux-v1.0.0.tar.gz
cd prl-miner-linux-v1.0.0
chmod +x setup.sh
./setup.sh
python main.py --wallet TU_WALLET
```

## Requisitos

- Linux (Ubuntu 20.04+)
- GPU AMD VEGA VII
- Python 3.8+
- ROCm 5.0+

## Descargas

- [prl-miner-linux-v1.0.0.tar.gz](https://github.com/xxfalaxx/prl-miner-amd/releases/download/v1.0.0-linux/prl-miner-linux-v1.0.0.tar.gz)
```

## 🆘 Solución de Problemas

### El archivo no sube
- **Problema:** Archivo muy grande
- **Solución:** GitHub tiene límite de 2GB por archivo. Comprime más o divide el contenido

### La etiqueta ya existe
- **Problema:** Intentas crear una etiqueta que ya existe
- **Solución:** Elimina con `git tag -d v1.0.0-linux` y `git push origin :v1.0.0-linux`

### El release no aparece
- **Problema:** Cambios no están en la rama correcta
- **Solución:** Verifica que usaste la rama correcta al crear el release

## 📚 Referencias

- [GitHub Releases Documentation](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
- [Git Tags Documentation](https://git-scm.com/book/en/v2/Git-Basics-Tagging)

---

**Versión de esta guía:** 1.0  
**Última actualización:** 11 de Septiembre de 2024
