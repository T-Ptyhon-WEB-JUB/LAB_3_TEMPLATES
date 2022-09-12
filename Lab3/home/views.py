from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from datetime import date
import string
import random

# Create your views here.

#############################################################################

def today(request : HttpRequest):

    today = date.today()
    
    return render(request, 'html/today.html', {"today" : today})




#############################################################################
def passgen(request : HttpRequest):
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    length : int = 8
    random.shuffle(characters)
    password = []

    for i in range(length):
        password.append(random.choice(characters))

    password = "".join(password)

    return render(request, 'html/password.html', {'password' : password})


#############################################################################
def favbook(request : HttpRequest):

    books = ["Book1", "Book2", "Book3", "Book4"]

    return render(request, 'html/books.html', {'books' : books})






