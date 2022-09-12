from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    # path('',views.index,name='index'),
    path('today/',views.home,name='home'),
    path('random/password/',views.password,name='home'),
    path('favs/books/',views.favBooks,name='home'),
]