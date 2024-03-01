from django.db import models

# Create your models here.
class CatalogoAnime(models.Model):
    nombre=models.CharField(max_length=50)
    genero=models.CharField(max_length=50)
    publicoObjaetivo=models.CharField(max_length=50)
    plataforma=models.CharField(max_length=50, choices=[("Netflix","Netflix"),("CrunchyRoll","CrunchyRoll"),("Youtube","Youtube"),("TV","TV")])
    fecha_creado=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre}-{self.genero}-{self.fecha_creado}"
    
class CatalogoManga(models.Model):
    nombre=models.CharField(max_length=50)
    genero=models.CharField(max_length=50)
    publicoObjaetivo=models.CharField(max_length=50)
    plataforma=models.CharField(max_length=50, choices=[("Webtoon","Webtoon"),("Crunchyroll Manga","Crunchyroll Manga"),("Youtube","Youtube")])
    fecha_creado=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre}-{self.genero}-{self.fecha_creado}"
    
class CatalogoVideojuegos(models.Model):
    nombre=models.CharField(max_length=50)
    genero=models.CharField(max_length=50)
    publicoObjaetivo=models.CharField(max_length=50)
    plataforma=models.CharField(max_length=50, choices=[("Xbox","Xbox"),("Playstation","Playstation"),("Computadora","Computadora")])
    fecha_creado=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre}-{self.genero}-{self.fecha_creado}"