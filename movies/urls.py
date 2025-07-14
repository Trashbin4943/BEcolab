from django.urls import path, include
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.MovieListView.as_view(), name='movielist'),
    path('<int:pk>/', views.MovieDetailView.as_view(), name='moviedetail'),
    path('<int:movie_pk>/comments/', views.movie_comments, name='moviecommentread'),
    path('<int:movie_pk>/comments/<int:pk>', views.movie_comments, name='moviecommentwrite'),
    path('directors/', views.DirectorListView.as_view(), name='director'),
    path('actors/',views.ActorListView.as_view(),name='actors'),
]