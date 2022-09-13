from django.urls import path
from . import views

urlpatterns = [
    path("fav/books/", views.fav_books, name="books")
]