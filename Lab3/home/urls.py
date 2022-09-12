from django.urls import path
from . import views


urlpatterns = [
    path('today/', views.today, name='today'),
    path('password/', views.passgen, name='password'),
    path('favs/books/', views.favbook, name='bookfavs'),
]