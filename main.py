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

@app.get("/release_date/{genres}")
def PlayTimeGenre(genres: str):
    df_filtered = play_genre[play_genre['genres'] == genres]

    if df_filtered.empty:
        return {"message": f"No se encontraron datos para el género {genres}"}

    usuario_año_playtime = df_filtered.groupby(['item_id', 'release_date'])['playtime_forever'].sum().reset_index()

    max_usuario = usuario_año_playtime.groupby('item_id')['playtime_forever'].sum().idxmax()

    df_max_usuario = usuario_año_playtime[usuario_año_playtime['item_id'] == max_usuario]

    max_usuario_año_playtime = df_max_usuario.groupby('release_date')['playtime_forever'].sum()

    max_usuario_año_playtime_list = [{"Año": str(year), "Horas": hours} for year, hours in max_usuario_año_playtime.items()]

    return {
        f"Genero con más horas jugadas  {genres}": max_usuario,
        "Horas jugadas": max_usuario_año_playtime_list
    }

if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True)

# Funcion def UserForGenre
@app.get("/user_genre/{genres}")

def UserForGenre(genres: str):
    
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
    '''Devuelve los 3 juegos más recomendados por usuarios para el año dado.'''
    
    filtrando_reviews = user_recommend[(user_recommend['release_date'].str.contains(str(year), regex=False, na=False)) & (user_recommend['recommend'] == True)]

    game_counts = filtrando_reviews['title'].value_counts().reset_index()
    game_counts.columns = ['title', 'count']

    top_games = game_counts.head(3)

    top_3_games_list = [{"Puesto {}: {}".format(i+1, game): count} for i, (game, count) in enumerate(zip(top_games['title'], top_games['count']))]

    return top_3_games_list

if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True)
    
    
# Funcion def juegosNoRecomendados
@app.get("/año")

def juegosNoRecomendados(año: int):
    
    ''' Y esta funcion lo que hara es lo contrario de la anterior, 
        devolvera los juegos no recomendados por los usuarios'''
        
    filtrando_reviews = juegos_no_recom[(juegos_no_recom['release_date'].str.contains(str(año), regex=False, na=False)) & (juegos_no_recom['recommend'] == False)]
    game_counts = filtrando_reviews['title'].value_counts().reset_index()
    game_counts.columns = ['title', 'count']
    
    juegos_no = game_counts.head(3)

    menos_3_juegos_list = [{"Puesto {}: ".format(i+1) + game: count} for i, (game, count) in enumerate(zip(juegos_no['title'], juegos_no['count']))]

    return menos_3_juegos_list

if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True)
    
    
# Función de Sentimiento   
@app.get("/anio")

def sentiment_analysis(anio:int):
    '''
    Función que devuelve la cantidad de registros de reseñas de usuarios 
    categorizados con un análisis de sentimiento para un año de lanzamiento específico. 
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