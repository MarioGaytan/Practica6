# Generated by Django 5.0.2 on 2024-03-01 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogoAnime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=50)),
                ('publicoObjaetivo', models.CharField(max_length=50)),
                ('plataforma', models.CharField(choices=[('Netflix', 'Netflix'), ('CrunchyRoll', 'CrunchyRoll'), ('Youtube', 'Youtube'), ('TV', 'TV')], max_length=50)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
