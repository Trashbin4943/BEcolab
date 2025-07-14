from rest_framework import serializers
from .models import Movie, Comment, Director, Actor 
from users.serializers import ProfileSerializer

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Director
        fields=['id','name','image_url']

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'character', 'image_url']

class MovieListSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(read_only=True)
    class Meta:
        model = Movie
        fields = ['id','title_kor','title_eng','poster_url','genre','rating','director']

class MovieDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(read_only=True, many=True)
    director = DirectorSerializer(read_only=True)
    class Meta:
        model = Movie
        fields = ['id','title_kor','title_eng','poster_url','genre','showtime','release_date','plot','rating','director','actors']

class CommentSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'rating', 'created_at', 'author']
        read_only_fields = ['created_at', 'author']   

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'rating']