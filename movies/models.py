from django.db import models
from django.conf import settings

#Director
class Director(models.Model):
    name=models.CharField(max_length=100)
    image_url=models.URLField()

    def __str__(self):
        return self.name

# acTOR
class Actor(models.Model):
    name=models.CharField(max_length=100)
    character=models.CharField(max_length=100)
    image_url=models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} as {self.character}"

#Movie
class Movie(models.Model):
    title_kor = models.CharField(max_length=200)
    title_eng = models.CharField(max_length=200, blank=True)
    poster_url = models.URLField(blank=True)
    genre = models.CharField(max_length=100, blank=True)
    showtime = models.CharField(max_length=50, blank=True)
    release_date = models.CharField(max_length=50,blank=True)
    plot = models.TextField(blank=True)
    rating = models.CharField(max_length=50, blank=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies',blank=True)
    
    def __str__(self):
        return self.title_kor
    
    
class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.author.username} - {self.movie.title_kor}({self.rating})"