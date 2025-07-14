from django.contrib import admin
from .models import Movie, Director, Actor, Comment

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title_kor','title_eng','genre','rating']
    search_fields = ['title_kor','title_eng']

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['name','character']
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['movie','author','content', 'created_at']
     