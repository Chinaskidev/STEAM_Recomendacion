from fastapi import FastAPI
import pandas as pd
import uvicorn

app = FastAPI()

# Lectura de todos los CSV
play_genre = pd.read_csv('PlayTimeGenre_funcion.csv', low_memory=False)
user_genre= pd.read_csv('UserForGenre_funcion.csv', low_memory=False)
user_recommend= pd.read_csv('UsersRecommend_funcion.csv', low_memory=False)
juegos_no_recom= pd.read_csv('UsersNotRecommend_funcion.csv', low_memory=False)
df_sentimiento_analisis= pd.read_csv('sentiment_analysis_funcion.csv', low_memory=False)

# Funcion def PlayTimeGenre

@app.get("/genero/{genres}")

def PlayTimeGenre(genres: str):
    df_filtered = play_genre[play_genre['genres'] == genres]

    if df_filtered.empty:
        return {"message": f"No se encontraron datos para el género {genres}"}

    max_playtime = (
        df_filtered.groupby(['item_id', 'release_date'])
        .agg(playtime_forever_sum=('playtime_forever', 'sum'))
        .groupby('item_id')
        .sum()
        .idxmax()
    )

    df_max_playtime = df_filtered[df_filtered['item_id'] == max_playtime[0]]
    max_playtime_by_year = df_max_playtime.groupby('release_date')['playtime_forever'].sum()

    max_playtime_list = [{"Año": str(year), "Horas": hours} for year, hours in max_playtime_by_year.items()]

    return {
        f"Genero con más horas jugadas {genres}": max_playtime,
        "Horas jugadas": max_playtime_list
    }


if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True)

# Funcion def UserForGenre
@app.get("/user_genre/{genres}")

def UserForGenre(genres: str):
    '''Función que devuelve al usuario con más horas jugadas para un género dado por año'''

    df_filtered = user_genre[user_genre['genres'] == genres]

    df_filtered = df_filtered[df_filtered['release_date'].str.match(r'\d{4}-\d{2}-\d{2}', na=False)]

    df_filtered['release_date'] = pd.to_datetime(df_filtered['release_date'], format='%Y-%m-%d')
    
    user_year_playtime = df_filtered.groupby(['user_id', df_filtered['release_date'].dt.year])['playtime_forever'].sum().reset_index()

    max_user = user_year_playtime.groupby('user_id')['playtime_forever'].sum().idxmax()

    df_max_user = user_year_playtime[user_year_playtime['user_id'] == max_user]

    max_user_year_playtime = df_max_user.groupby('release_date')['playtime_forever'].sum()

    max_user_year_playtime_list = [{"Año": year, "Horas": hours} for year, hours in zip(max_user_year_playtime.index, max_user_year_playtime)]

    return {
        f"Usuario con más horas jugadas para {genres}": max_user,
        "Horas jugadas": max_user_year_playtime_list
    }

# Funcion def UsersRecommend
@app.get("/year")

def UsersRecommend(year: int):
    '''Devuelve los 3 juegos más recomendados por usuarios para el año dado por un usuario específico.'''

    # Filtrar reseñas recomendadas para el año y el usuario específico
    filtered_reviews = user_recommend[(user_recommend['release_date'].str.contains(str(year), regex=False, na=False)) & (user_recommend['recommend'] == True)]

    # Contar la cantidad de reseñas por título de juego y seleccionar los 3 juegos más recomendados
    top_games = (
        filtered_reviews['title']
        .value_counts()
        .head(3)
        .reset_index()
        .rename(columns={'index': 'title', 'title': 'count'})
    )

    # Crear una lista de diccionarios con los juegos más recomendados
    top_3_games_list = [{f"Puesto {i+1}: {game}": count} for i, (game, count) in top_games.iterrows()]

    return top_3_games_list

if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True)
    
    
# Funcion def juegosNoRecomendados
@app.get("/año")

def juegosNoRecomendados(año: int):
    '''Devuelve los juegos menos recomendados por usuarios para el año dado.'''

    filtered_reviews = juegos_no_recom[(juegos_no_recom['release_date'].str.contains(str(año), regex=False, na=False)) & (juegos_no_recom['recommend'] == False)]

    less_rated_games = (
        filtered_reviews['title']
        .value_counts()
        .head(3)
        .reset_index()
        .rename(columns={'index': 'title', 'title': 'count'})
    )

    less_3_games_list = [{f"Puesto {i+1}: {game}": count} for i, (game, count) in less_rated_games.iterrows()]

    return less_3_games_list


if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True)
    
    
# Función de Sentimiento   
@app.get("/anio")

def sentiment_analysis(anio):
    '''
    Función que devuelve la cantidad de registros de reseñas de usuarios 
    categorizados con un análisis de sentimiento para un anio de lanzamiento específico. 
    '''
    df_filtrado = df_sentimiento_analisis[df_sentimiento_analisis['release_date'].str.startswith(str(anio))]

    sentiment_counts = df_filtrado['sentiment_analysis'].value_counts()

    result_dict = {"Negative": 0, "Neutral": 0, "Positive": 0}
    
    for index, count in sentiment_counts.items():
        if index == 0:
            result_dict["Negative"] = count
        elif index == 1:
            result_dict["Neutral"] = count
        elif index == 2:
            result_dict["Positive"] = count

    return result_dict


if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True)