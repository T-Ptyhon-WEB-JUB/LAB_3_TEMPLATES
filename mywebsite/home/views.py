from django.shortcuts import render

# Create your views here.


def today(requset):
    return render("", 'home/today.html')


def password(requset):
    return render("", 'home/password.html')


def book(requset):
    return render("", 'home/book.html')
