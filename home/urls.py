from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("today/",  views.tody, name="today"),
    path("random/password/",  views.password, name="pas"),
    path("favs/books/",  views.book, name="book")
]