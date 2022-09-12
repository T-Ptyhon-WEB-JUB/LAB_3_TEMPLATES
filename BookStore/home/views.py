from datetime import date
import string
import random
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def today(request : HttpRequest):
    from datetime import date
    today = date.today()
       
    return render(request, 'home/today.html', {"today" : today})

def get_random(request : HttpRequest):

    random_pass = "".join(random.choices(string.ascii_letters, k= 9))

    return render(request, 'home/random.html', {"random_pass" : random_pass})


def books(request : HttpRequest):

    books = ["1","2","3",'4']

    return render(request, 'home/books.html', {"books" : books})