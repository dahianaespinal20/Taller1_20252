
from django.core.management.base import BaseCommand
from movie.models import Movie
import os
import json
class Command(BaseCommand):
   help = 'Load movies from movies.json into the Movie model'
   def handle(self, *args, **kwargs):
       # Ruta exacta donde debe estar el JSON (junto a este archivo)
       json_file_path = os.path.join('movie', 'management', 'commands', 'movies.json')
       if not os.path.exists(json_file_path):
           self.stderr.write(f'No se encontró {json_file_path}. Coloca allí movies.json.')
           return
       # Cargar datos
       with open(json_file_path, 'r', encoding='utf-8') as file:
           movies = json.load(file)
       limite = min(100, len(movies))
       creadas = 0
       for i in range(limite):
           movie = movies[i] or {}
           title = str(movie.get('title') or '').strip()
           if not title:
               continue  # sin título no insertamos
           # Evitar duplicados por título
           if Movie.objects.filter(title=title).first():
               continue
           genre = str(movie.get('genre') or '').strip()
           # Año seguro
           year_raw = movie.get('year')
           try:
               year = int(year_raw) if year_raw not in (None, '') else 0
           except (ValueError, TypeError):
               year = 0
           # Descripción segura: acepta 'plot' o 'description' y nunca None
           description = str(movie.get('plot') or movie.get('description') or '').strip()
           Movie.objects.create(
               title=title,
               image='movie/images/default.jpg',   # si tu archivo es 'default.JPG', cámbialo aquí
               genre=genre,
               year=year,
               description=description
           )
           creadas += 1
       self.stdout.write(self.style.SUCCESS(f'Películas creadas: {creadas} desde {json_file_path}'))