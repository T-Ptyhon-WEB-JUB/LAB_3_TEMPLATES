from importlib.resources import path
from django.urls import path
from . import views

app_name = "thamerLab3"

urlpatterns = [
    path("today/", views.today, name= "today"),
    path("random/password/", views.password, name= "password"),
    path("favs/books/", views.books, name = 'books')
]