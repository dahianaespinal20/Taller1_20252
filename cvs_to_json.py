import pandas as pd
import json

# 1) lee el CSV (ajusta el nombre si cambia)
df = pd.read_csv("movies_initial.csv")
df.to_json("movies.json", orient="records")

with open( 'movies.json', 'r') as file:
    movies = json.load(file)

for i in range (100):
    movie =movies [i]
    print (movie)
    break


