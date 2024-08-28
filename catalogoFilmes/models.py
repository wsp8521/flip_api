from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


#Genero
class Genre(models.Model):
    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"
    name = models.CharField(max_length=200, verbose_name='Gênero')

    def __str__(self):
        return self.name

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#Actor model
NATIONALITY=(('Estados Unidos',"USA"),('Brasil', 'Brazil'),)
class Actor(models.Model):
    class Meta:
        verbose_name = "Ator"
        verbose_name_plural = "Atores"

    nameActor=models.CharField(max_length=200, verbose_name="Nome do ator")
    birthday_date = models.DateField(blank=True, null=True, verbose_name="Data de nascimento")
    nationality = models.CharField(max_length=100, choices=NATIONALITY,verbose_name="Nacionalidade")

    def __str__(self):
        return self.nameActor

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Movie
class Movie(models.Model):
    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"

    title = models.CharField(max_length=250, verbose_name="Título")
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, verbose_name='Gênero', related_name='movie')
    actors = models.ManyToManyField(Actor,verbose_name='Atores')
    realese_data=models.DateField(blank=True, null=True, verbose_name='Data de lançamento')
    sinpse=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#Reviews
class Reviews(models.Model):
    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliaçõe"

    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, verbose_name='Filme', related_name='reviws') 
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0,'informe um valor entre 0 e 5'),
            MaxValueValidator(5,'infome o valor entre 0 e 5') 
        ])
    comment = models.TextField(blank=True, null=True)

   



