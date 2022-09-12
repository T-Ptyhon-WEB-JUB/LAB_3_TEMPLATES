from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("today/", views.today, name="today"),
    path("random/password/", views.password, name="password"),
    path("favs/books/", views.book, name="book")
]
