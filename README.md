# Consulting & IT Employer Reputation Intelligence

Este proyecto analiza la reputación empleadora de Accenture frente a sus principales competidores a partir de reseñas de Glassdoor. La metodología combina minería de texto, análisis de sentimiento, topic modeling y comparación entre empresas para identificar fortalezas, debilidades y oportunidades de mejora en su marca empleadora.

## Objetivo del proyecto

El objetivo es evaluar cómo percibe Accenture a sus empleados y candidatos en comparación con empresas del mismo sector, identificando los temas recurrentes en las reseñas y transformando esos resultados en una narrativa clara y útil para stakeholders o equipos de RRHH.

## Estructura del repositorio

- `notebooks/consulting-it-employer-reputation-intelligence.ipynb` — notebook principal de análisis exploratorio.
- `docs/` — documentación y material de referencia.
- `data/raw/` — datos brutos del proyecto. El dataset grande de reseñas se mantiene local y no se publica en GitHub.
- `requirements.txt` — dependencias necesarias para ejecutar el proyecto.
- `.gitignore` — exclusiones del entorno local y outputs generados.

## Assets locales

Los siguientes archivos se mantienen fuera del repositorio público porque son pesados o específicos de la presentación final:

- `data/raw/glassdoor_reviews_hr.parquet` — dataset grande usado localmente para el análisis.
- `scripts/build_powerpoint.py` — script local para generar la presentación.
- `src/presentation/` — lógica local de exportación a PowerPoint.
- `output/` — gráficas y archivos generados.

## Configuración del entorno

En Windows PowerShell:

```powershell
cd "C:\Users\midef\Documents\Consulting & IT Employer Reputation Intelligence"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Ejecución del análisis

```powershell
cd "C:\Users\midef\Documents\Consulting & IT Employer Reputation Intelligence"
.\.venv\Scripts\Activate.ps1
jupyter notebook notebooks\consulting-it-employer-reputation-intelligence.ipynb
```

## Nota sobre datos y presentación

Este repositorio está pensado para mantener público el flujo analítico y la documentación, mientras se protege la parte de datos pesados y la generación de la presentación final. El notebook es la fuente principal de evidencia, y la PowerPoint se genera localmente cuando se necesita para la defensa o entrega a stakeholders.

## Estado del proyecto

El repositorio contiene la base analítica, la documentación y el flujo reproducible del estudio. Los datos grandes y la lógica de presentaciones permanecen en el entorno local para mantener el repositorio de GitHub ligero y funcional.
