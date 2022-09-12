from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import secrets
# Create your views here.
def home (request):
    return (
        render(request,'home/index.html',{'today':date.today})  #to return a templete
    )
def password(request):
    passwordlen=10
    return(
        render(request,'password/pass.html',{'pass':secrets.token_urlsafe(passwordlen)})
    )       
def favBooks(request):
    booksList=['book1','book2','book3']
    return(
        render(request,'FavBooks/fav.html',{'books':booksList})
    )
