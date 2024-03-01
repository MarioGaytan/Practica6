from rest_framework import serializers
from .models import CatalogoAnime, CatalogoManga, CatalogoVideojuegos

class CatalogoAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model=CatalogoAnime
        fields='__all__'
        
class CatalogoMangaSerializer(serializers.ModelSerializer):
    class Meta:
        model=CatalogoManga
        fields='__all__'

class CatalogoVideojuegosSerializer(serializers.ModelSerializer):
    class Meta:
        model=CatalogoVideojuegos
        fields='__all__'