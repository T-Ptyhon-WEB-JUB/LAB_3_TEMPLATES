from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("today/",  views.date_today, name="today"),
    path("random/password/",  views.password , name="pass"),
    path("favs/books/",  views.book, name="books")
] 