<h1 align="center"> MLOps Juegos Steam - Modelo de recomendación </h1>

<h4 align="center"> Este repositorio alberga el Proyecto Individual 1 de Machine Learning realizado durante el bootcamp de Henry. </h4>


 <p align="center">
  <img src="https://img.shields.io/badge/Python-green">
  <img src="https://img.shields.io/badge/Numpy-aqua">
  <img src="https://img.shields.io/badge/Pandas-blue">
  <img src="https://img.shields.io/badge/Matplotlib-grey">
  <img src="https://img.shields.io/badge/Seaborn-aquamarine">
  <img src="https://img.shields.io/badge/FastApi-darkseagreen">
  <img src="https://img.shields.io/badge/Scikitlearn-orange">
  <img src="https://img.shields.io/badge/Render-cyan">
  <img src="https://img.shields.io/badge/TextBlob-black">
</p>


<p align="center">
  <img src="./imagen/steam.png" alt="STEAM" width="600">
</p>


<h1 align="center"> Desarrollo del Sistema de Recomendación para STEAM </h1>

## Descripción del proyecto:

- Este proyecto se enfoca en el desarrollo de un sistema de recomendación para la plataforma de videojuegos STEAM, el cual se nos ha dado un rol de MLOps Engineer. En el cúal se implementó un proceso de Extracción, Transformación y Carga (ETL) para afrontar la llegada de datos en formato JSON. Esto incluyó un minucioso desanidamiento y limpieza de los datos. 

- En el transcurso del EDA, se llevó a cabo un análisis profundo para comprender la naturaleza de los datos. Esto abarcó un estudio de sentimientos aplicando la librería TextBlob a una de las columnas que contenía los comentarios de los usuarios en el dataset de user_reviews. El resultado fue la creación de una nueva columna que clasifica los sentimientos, utilizando la biblioteca TextBlob, una herramienta de Procesamiento del Lenguaje Natural (NLP). Este procedimiento implicó la evaluación de la polaridad del sentimiento en cada comentario, categorizándolos como negativos, neutrales o positivos.

## Preparación de Datos y Optimización

Además de la metodología descrita, se realizaron tareas de preparación específica de los datasets para cada función. Esto permitió optimizar los tiempos y el rendimiento del servicio en la nube, facilitando el despliegue eficiente de la API y resolviendo consultas con mayor eficacia. 
