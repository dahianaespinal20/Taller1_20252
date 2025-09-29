from django.urls import path
from . import views   # importa las vistas de esta app

urlpatterns = [
    path('', views.news, name='news'),  
]
