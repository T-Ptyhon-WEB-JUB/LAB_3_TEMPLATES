import random
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import secrets
from datetime import date
# Create your views here.


def home(request : HttpRequest):
  ##home="111"
  return render(request, "hom/index.html",{"ss":home}) 

def password(request: HttpRequest):
  random_pass = "".join(random.choices(["Q","r","$","m","c"], k=9))
  
  return render(request, "hom/password.html",{"pass":random_pass}) 

def today(request: HttpRequest):
  today = date.today()
  return render(request, "hom/today.html",{"todate":today})

def books(request: HttpRequest):
  books = ["the gun","the sky","thg redar","big_boss","tiger"]
  return render(request, "hom/books.html",{"books":books})
