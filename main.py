from fastapi import FastAPI
import pandas as pd
import uvicorn

app = FastAPI()

# Lectura de todos los CSV
play_genre = pd.read_csv('PlayTimeGenre_funcion.csv', low_memory=False)

# Funcion 1

@app.get("/genero/{genres}")
def PlayTimeGenre(genres):
    # Filtrar por el género proporcionado
    df_filtered = play_genre[play_genre['genres'] == genres]

    if df_filtered.empty:
        return {"message": f"No se encontraron datos para el género {genres}"}

    # Encontrar el índice del item con más tiempo jugado
    max_playtime_index = df_filtered['playtime_forever'].idxmax()

    # Obtener el año y las horas jugadas
    max_playtime_year = df_filtered.loc[max_playtime_index, 'release_date']
    max_playtime_hours = df_filtered.loc[max_playtime_index, 'playtime_forever']

    return {
        f"Genero con más horas jugadas {genres}": {
            "Año": str(max_playtime_year),
            "Horas": max_playtime_hours
        }
    }

if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True)