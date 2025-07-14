from django.urls import path, include
from . import views

app_name='users'
urlpatterns = [
    path('profile/', views.profile, name='user-profile'),
]