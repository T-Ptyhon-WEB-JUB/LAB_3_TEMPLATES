from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('today/', views.today, name='home'),
    path('random/password/', views.random_password, name='home'),
    path('favs/books/', views.fav_books, name='home'),
]
