from . import views
from django.urls import path

app_name = "home"

urlpatterns = [
    path("", views.home, name ="home"),
    path("Random/password/",views.password, name=""),
    path("Today/",views.today, name= ""),
    path("favs/books/",views.books, name="")
]