# Employer Reputation Intelligence — Accenture case

Este proyecto analiza la reputación empleadora de Accenture frente a sus peers principales en Glassdoor, combinando análisis de texto, topic modeling y comparación de fortalezas/debilidades entre empresas.

## Estructura del proyecto

- `docs/`: documento oficial del caso práctico y material de referencia.
- `notebooks/Glassdoor_ejemplo.ipynb`: notebook principal del análisis.
- `data/raw/`: datos brutos del proyecto (`.parquet` y `.xlsx`).
- `src/presentation/`: lógica para exportar la presentación PowerPoint.
- `scripts/build_powerpoint.py`: script ejecutable para generar la PPT.
- `output/`: resultados y gráficas exportadas.
- `requirements.txt`: dependencias del entorno Python.

## Entorno virtual

En Windows PowerShell:

```powershell
cd "C:\Users\midef\Documents\Consulting & IT Employer Reputation Intelligence"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Ejecutar el notebook

```powershell
cd "C:\Users\midef\Documents\Consulting & IT Employer Reputation Intelligence"
.\.venv\Scripts\Activate.ps1
jupyter notebook notebooks\Glassdoor_ejemplo.ipynb
```

## Generar la presentación PowerPoint

```powershell
cd "C:\Users\midef\Documents\Consulting & IT Employer Reputation Intelligence"
.\.venv\Scripts\Activate.ps1
python scripts/build_powerpoint.py
```

Esto genera el archivo PPTX en `output/`.

## Git

Inicializa y aplica el primer commit cuando ya esté la estructura básica estable:

```bash
git init
git add .
git commit -m "Initial project structure"
```

Luego podrás conectarlo a GitHub:

```bash
git branch -M main
git remote add origin <URL_DEL_REPO>
git push -u origin main
```
