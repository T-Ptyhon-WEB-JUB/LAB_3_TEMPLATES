from django.urls import path
from . import views



urlpatterns = [
    path('today/', views.today, name= "today"),
    path('random/password/', views.get_random, name = "get_random"),
    path('fav/books/', views.books, name = "books")
]