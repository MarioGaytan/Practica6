from django.contrib import admin
from .models import CatalogoAnime, CatalogoManga, CatalogoVideojuegos
# Register your models here.
admin.site.register(CatalogoAnime)
admin.site.register(CatalogoManga)
admin.site.register(CatalogoVideojuegos)