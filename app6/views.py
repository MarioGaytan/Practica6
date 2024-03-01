from django.shortcuts import render

# Create your views here.
from .serializer import CatalogoAnimeSerializer, CatalogoMangaSerializer, CatalogoVideojuegosSerializer
from .models import  CatalogoAnime, CatalogoManga, CatalogoVideojuegos
from rest_framework import viewsets

class  CatalogoAnimeViewSet(viewsets.ModelViewSet):
    queryset = CatalogoAnime.objects.all()
    serializer_class=CatalogoAnimeSerializer
    
class  CatalogoMangaViewSet(viewsets.ModelViewSet):
    queryset = CatalogoManga.objects.all()
    serializer_class=CatalogoMangaSerializer
    
class  CatalogoVideojuegosViewSet(viewsets.ModelViewSet):
    queryset = CatalogoVideojuegos.objects.all()
    serializer_class=CatalogoVideojuegosSerializer