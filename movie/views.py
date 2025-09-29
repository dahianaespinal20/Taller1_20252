from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
 
import matplotlib.pyplot as plt 
import matplotlib 
import io 
import urllib, base64 
from collections import Counter
from io import BytesIO
import base64
from collections import Counter
matplotlib.use('Agg')

# imports (arriba del archivo)





# Create your views here.
#def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    #return render(request, 'home.html')
    #return render(request,'home.html',{'name':'Leidy Espinal'})
    #searchTerm = request.GET.get('searhMovie')
    #if searchTerm:
        #movies = Movie.objects.filter(title__icontains=searchTerm)
    #else:
        #movies = Movie.objects.all
    #return render(request, 'home.html',{'searchTem':searchTerm, 'movies':movies})

def about(request):
    #return HttpResponse('<h1>Welcome to About Page</h1>')
    return render(request, "about.html")

def home(request):
    searchTerm = request.GET.get('searchMovie')  # 👈 debe coincidir con el input name
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {
        'searchTerm': searchTerm,
        'movies': movies
    })
def signup(request):
    email= request.GET.get('email')
    return render(request, 'signup.html', {'email':email})
def _to_png_and_close():
   buf = BytesIO()
   plt.tight_layout()
   plt.savefig(buf, format='png')
   plt.close()
   buf.seek(0)
   return base64.b64encode(buf.getvalue()).decode('utf-8')
def statistics_view(request):
   import matplotlib; matplotlib.use('Agg')
   import matplotlib.pyplot as plt
   from io import BytesIO
   import base64
   from collections import Counter
   movies = Movie.objects.all()
   # --- conteo por año ---
   c_year = Counter(int(m.year or 0) for m in movies)
   c_year.pop(0, None)
   years = sorted(c_year)
   year_counts = [c_year[y] for y in years]
   # --- conteo por género (primer género) ---
   def first_genre(s):
       s = (s or "").replace("/", ",")
       return (s.split(",")[0].strip() or "None")
   c_gen = Counter(first_genre(m.genre) for m in movies)
   genres = list(c_gen.keys())
   genre_counts = [c_gen[g] for g in genres]
   # --- una figura con dos subplots ---
   fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
   ax1.bar(years, year_counts)
   ax1.set_title("Movies per year")
   ax1.set_xlabel("Year"); ax1.set_ylabel("Movies")
   ax2.bar(genres, genre_counts)
   ax2.set_title("Movies per genre (first)")
   ax2.set_xlabel("Genre"); ax2.set_ylabel("Movies")
   ax2.tick_params(axis="x", rotation=45)
   plt.tight_layout()
   buf = BytesIO()
   fig.savefig(buf, format="png")
   plt.close(fig)
   buf.seek(0)
   graphic = base64.b64encode(buf.getvalue()).decode("utf-8")
   return render(request, "statistics.html", {"graphic": graphic})

