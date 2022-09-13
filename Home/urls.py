from django.urls import path
from . import views

app_name = "Home"

urlpatterns = [
    path("today/",  views.tody, name="today"),
    path("random/password/",  views.pas, name="pas"),
    path("", views.home, name="home")
]   