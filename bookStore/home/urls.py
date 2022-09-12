from urllib.parse import urlparse
from django.urls import path
from home import views

mhyapp = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path("today/", views.today, name="today"),
    path("random/password/", views.passing, name="password"),
    path("favs/books/", views.favs_books , name="books")
]   