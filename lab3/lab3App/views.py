from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import secrets
from datetime import date


# Create your views here.
def today(request):
    today = date.today()
    #
    # # the key passed to the index.html "msg"
    return render(request, 'lab3App/today.html',{"today":today})

def password(request):
    password_length = 13
    pass_word = secrets.token_urlsafe(password_length)
    return render(request, 'lab3App/password.html',{"password":pass_word})
    
def books(request):
    books = ["Student's Book 3","The Upstarts: How Uber, Airbnb And The Killer Companies Of The New Silicon Valley","Seventeen - Attacca"]
    return render(request, 'lab3App/books.html',{"books":books})
    