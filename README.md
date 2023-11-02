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
  <img src="./imagen/steam.png" alt="STEAM" width="400">
</p>


<h1 align="center"> Desarrollo del Sistema de Recomendación para STEAM </h1>

## Descripción del proyecto:

- Este proyecto se enfoca en el desarrollo de un sistema de recomendación para la plataforma de videojuegos STEAM, donde se ha asumido el rol de MLOps Engineer. Se ha implementado un proceso de Extracción, Transformación y Carga (ETL) y un Análisis Exploratorio de Datos (EDA). El objetivo principal es desplegar una API con un modelo de Machine Learning capaz de analizar los sentimientos a partir de los comentarios de los usuarios. Este modelo también servirá para ofrecer un sistema de recomendación de videojuegos para la plataforma, mejorando la experiencia de los usuarios.


## Fases del Proyecto

El proyecto se diseñó siguiendo una estructura basada en principios fundamentales que abarcan distintas etapas:

- ETL (Extracción, Transformación y Carga): Proceso de tratamiento de datos para asegurar su adecuada preparación. [ETL](https://github.com/Chinaskidev/STEAM_Recomendacion/blob/master/PI_etl.ipynb)

- EDA (Análisis Exploratorio de Datos): Análisis en profundidad para comprender la naturaleza y características de los datos. [EDA](https://github.com/Chinaskidev/STEAM_Recomendacion/blob/master/PI_EDA.ipynb)
- Funciones (endpoints) para el funcionamiento de la API: Implementación de funcionalidades clave para el funcionamiento de la interfaz de programación de aplicaciones. [Funciones](https://github.com/Chinaskidev/STEAM_Recomendacion/blob/master/funciones.ipynb)
- Modelos de Aprendizaje: Desarrollo de modelos de Machine Learning para el análisis y recomendación de datos. [Modelo](https://github.com/Chinaskidev/STEAM_Recomendacion/blob/master/main.py)
- Implementación de la API utilizando RENDER para el despliegue: Proceso de despliegue utilizando la plataforma RENDER para asegurar su disponibilidad y funcionalidad.

## ETL (Extracción, Transformación y Carga)

Durante esta etapa, enfrentamos el desafío de procesar datos desde archivos en formato JSON a archivos CSV. Este proceso incluyó la identificación y corrección de codificaciones, así como la transformación de datos,limpieza y  además de la tarea de desanidar archivos. Llevar a cabo esta labor implicó una investigación exhaustiva para garantizar la integridad y coherencia de los datos resultantes.

- Aqui los archivos trabajados en el ETL [Datasets](https://github.com/Chinaskidev/STEAM_Recomendacion/blob/master/imagen/archivos_proyecto.png)

## EDA (Análisis Exploratorio de Datos)
Durante esta fase, se realizó un análisis minucioso de los datos, lo cual resultó en una experiencia fascinante al observar los datos limpios y trabajar en su comprensión más profunda. Se llevó a cabo una limpieza  para tratar valores nulos y se realizaron representaciones gráficas con el objetivo de obtener una comprensión más profunda de la integridad y naturaleza de nuestros datos. Este proceso permitió identificar patrones, tendencias y particularidades esenciales, brindando así una base sólida para la siguiente etapa de desarrollo del proyecto.


- Feature Engineering

Dentro del dataset de user_reviews, se recopilan reseñas de juegos realizadas por diversos usuarios. Como parte del desafío de negocio, se me asignó la tarea de crear una columna de sentimiento. Para llevar a cabo esta tarea, se empleó una librería de Procesamiento del Lenguaje Natural (NLP) TextBlob ,con el fin de generar esta columna de sentimiento. Se estableció una escala donde el valor '0' corresponde a una valoración negativa, '1' indica neutralidad y '2' representa una valoración positiva. Este enfoque permitió categorizar las reseñas en base a su sentimiento, proporcionando así una capa adicional de comprensión y análisis en el dataset.

Acá el trabajo realizado: [EDA](https://github.com/Chinaskidev/STEAM_Recomendacion/blob/master/PI_EDA.ipynb)

## Construcción de la API

Para el desarrollo de la API, he empleado el framework FASTAPI. A continuación, se detallan las funciones creadas para los endpoints que serán consumidos en nuestra API:

1. PlayTimeGenre(genero): Esta función devuelve el año con la mayor cantidad de horas jugadas para el género especificado.

2. UserForGenre(genero): La función UserForGenre devuelve el usuario que acumula la mayor cantidad de horas jugadas para el género especificado, junto con una lista que muestra la acumulación de horas jugadas por año.

3. UsersRecommend(año): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. Estos juegos tienen recomendaciones positivas o neutrales y cuentan con la máxima calificación por parte de los usuarios.

4. UsersNotRecommend(año): Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. Estos juegos tienen recomendaciones negativas y comentarios críticos por parte de los usuarios.

5. sentiment_analysis(año): Esta función devuelve una lista que muestra la cantidad de registros de reseñas de usuarios categorizadas con un análisis de sentimiento, según el año de lanzamiento. La lista desglosa la cantidad de reseñas positivas, negativas y neutrales para ese año.

Estas funciones son fundamentales para el funcionamiento de nuestra API, ya que se encargan de procesar las solicitudes entrantes y generar respuestas adecuadas.

Acá el trabajo realizado: [Funciones-API](https://github.com/Chinaskidev/STEAM_Recomendacion/blob/master/funciones.ipynb)

## Modelamiento (Machine Learning)

En esta fase del proyecto, se llevó a cabo el modelado para el desarrollo del Sistema de Recomendación, basado en la similitud del coseno, donde se crearon las siguientes funciones:

- Primera Función item-item, introduzco el id del juego y me devuelve juegos recomendados.

- Segunda Función de usuario-item, Ingreso el id  del usuario y le devuelve juegos recomendados.

Para el primer enfoque del modelo, se establece una relación ítem-ítem. En este escenario, se evalúa un ítem con respecto a su similitud con otros ítems para ofrecer recomendaciones similares. En este caso, el input corresponde a un juego y el output es una lista de juegos recomendados, utilizando el concepto de similitud del coseno.

Por otra parte, se considera una segunda propuesta para el sistema de recomendación, basada en el filtro user-item. En esta estrategia, se analiza a un usuario para identificar usuarios con gustos similares y se recomiendan ítems que hayan sido apreciados por estos usuarios afines.

Acá el trabajo realizado: [Modelo/Machine-Learning](https://github.com/Chinaskidev/STEAM_Recomendacion/blob/master/main.py)

## FastAPI

Si deseaejecutar la API desde el localhost debe seguir los siguientes pasos: 

- Clonar el proyecto haciendo git clone **git@github.com:Chinaskidev/STEAM_Recomendacion.git**

- Preparación del entorno de trabajo en **Visual Studio Code**

* Crear entorno **python -m venv** entorno (o el nombre que usted desee)

* Ingresar al entorno haciendo **entorno\bin\activate**, en el caso si usa Windows entorno\Scripts\activate

- Instalar dependencias con **pip install -r requirements.txt**

- Ejecutar el archivo **main.py** desde consola activando uvicorn. Si usted importa la libreria uvicorn en el archivo main.py, desde la consola escribir python main.py y correra facilmente. De lo contrario puedes hacer uvicorn main:app --reload

- Hacer Ctrl + clic sobre la dirección **http://XXX.X.X.X:XXXX**  (eso se visualizara en su Terminal).

- Una vez en el navegador, **agregar /docs para acceder**.

- En cada una de las funciones hacer clic en **Try it out** y luego introducir el dato que requiera o utilizar los ejemplos por defecto. 

- Finalmente Ejecutar y observar la respuesta. **Felicidades has creado un Sistema de Recoemndacion!!!**


## Render/Deploy

Para llevar a cabo el despliegue, utilicé la plataforma [RENDER](https://www.render.com) un entorno que facilita la creación y ejecución de aplicaciones y sitios web. Esta plataforma permite el despliegue automático de los desarrollos directamente desde GitHub, proporcionando una integración sencilla y eficiente con el repositorio de código.

## Conclusión

Este proyecto representó una travesía emocionante y enriquecedora. A lo largo de este trayecto, he aprendido no solo sobre el funcionamiento de un sistema de recomendación, sino también sobre la importancia de las fases iniciales como el ETL y el EDA. La comprensión a fondo de los datos y la limpieza rigurosa son fundamentales para cualquier desarrollo. Además, la implementación de una API con FastAPI y el despliegue con Render han sido experiencias valiosas que han ampliado mi comprensión de cómo llevar a producción un proyecto de Machine Learning.

En resumen, este proyecto no solo ha mejorado mis habilidades técnicas, sino que también ha reforzado la importancia de la planificación y la comprensión de los datos en cada etapa del proceso. 