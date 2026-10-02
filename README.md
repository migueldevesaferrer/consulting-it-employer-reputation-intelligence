# Consulting & IT Employer Reputation Intelligence

Este proyecto analiza la reputación de la empleadora de Accenture frente a sus principales competidores a partir de reseñas de Glassdoor. La metodología combina procesamiento del lenguaje natural, análisis de sentimiento, modelado de tópicos y comparación entre empresas para identificar fortalezas, debilidades y oportunidades de mejora en la percepción de la marca empleadora.

## Objetivo del proyecto

El objetivo es evaluar cómo se percibe a Accenture como empleadora en comparación con otras empresas del mismo sector, identificando los temas recurrentes en las reseñas y transformando esos resultados en una narrativa clara y útil para stakeholders o equipos de RRHH.

## Estructura del repositorio

- `notebooks/consulting-it-employer-reputation-intelligence.ipynb` — notebook principal de análisis exploratorio.
- `data/raw/` — datos brutos del proyecto. El dataset grande de reseñas se mantiene local y no se publica en GitHub.
- `requirements.txt` — dependencias necesarias para ejecutar el proyecto.
- `requirements-lock.txt` — versiones exactas del entorno validado (Windows, Python 3.13.14).
- `.gitignore` — exclusiones del entorno local y outputs generados.

## Datos locales

Los siguientes archivos se mantienen fuera del repositorio público por tamaño o privacidad:
- `data/raw/glassdoor_reviews_hr.parquet` — dataset grande usado localmente para el análisis.
- `docs/Caso_Practico_NLP_Glassdoor_RRHH.pdf` — enunciado del ejercicio, mantenido local por privacidad y para no revelar el origen del caso.
- `output/` — gráficas y tablas generadas por el notebook.

## Configuración del entorno

En Windows PowerShell:

```powershell
cd "C:\Users\midef\Documents\Consulting & IT Employer Reputation Intelligence"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-lock.txt
```

`requirements-lock.txt` reproduce la ejecución analítica validada. Para instalar rangos de versiones más flexibles, usar `python -m pip install -r requirements.txt`.

## Ejecución del análisis

```powershell
cd "C:\Users\midef\Documents\Consulting & IT Employer Reputation Intelligence"
.\.venv\Scripts\Activate.ps1
jupyter notebook notebooks\consulting-it-employer-reputation-intelligence.ipynb
```

## Alcance

El repositorio conserva el flujo analítico y la documentación. Los datos de origen y los resultados generados se mantienen localmente; el notebook es la fuente principal de evidencia del estudio.

## Estado del proyecto

El repositorio contiene la base analítica, la documentación y el flujo reproducible del estudio. Los datos grandes y los archivos generados permanecen en el entorno local para mantener el repositorio ligero y funcional.
