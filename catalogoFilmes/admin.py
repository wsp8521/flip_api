from django.contrib import admin
from catalogoFilmes.models import Genre, Actor, Movie,Reviews


@admin.register(Genre)
class GeneroAdmin(admin.ModelAdmin):
    list_display=("id","name")
    list_display_links=("name",)

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display=('id','nameActor')
    list_display_links=("nameActor",)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display=('id','title', 'genre',)
    list_display_links=("title",)

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
        list_display=('id','movie','stars','comment',)
        list_display_links=("movie",)