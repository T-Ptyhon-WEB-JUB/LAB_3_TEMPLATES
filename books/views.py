from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random 
import datetime
# Create your views here.
def date_today(request : HttpRequest):
    time = datetime.date.today()
    return render(request, 'books/index.html', {"date": time})

def password(request):

    characters = list('0987654321abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    password = ''
    for x in range(12):
        password += random.choice(characters)
    return render(request, 'books/pass.html', {'pass':password}) 

def book(request : HttpRequest):
    book = ["Netowrk Systems ", "Human Computer Interaction", "Socail Ethics"]
    return render(request, 'books/book.html', { "book" : book})