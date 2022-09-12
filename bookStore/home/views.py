from django.shortcuts import render
from django.http import HttpRequest, HttpResponse



def home(request : HttpRequest):
    return render(request , "file/index.html" )

from datetime import date
todays = date.today()

def today(request : HttpRequest):
    return render(request , "file/today.html" , {"todays" : f"today is {todays}"})

mybooks = ["The best world","bash","program whit py","liunx","my world"]

def favs_books(request : HttpRequest):
    return render(request , "file/books.html" , {"mybooks" : mybooks})


import random
data = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"

def Getpass(data):
             Max = 12
             password = ""
             while len(password) != Max:
                 Val = random.choice(data)
                 password += Val
             return password

def passing(request : HttpRequest):
    return render(request , "file/password.html" , {"send" : f"your pass is {Getpass(data)}" })

