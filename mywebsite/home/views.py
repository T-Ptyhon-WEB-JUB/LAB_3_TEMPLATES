from django.shortcuts import render
from datetime import date
# Create your views here.


def today(requset):
    today_date = date.today()
    return render("", 'home/today.html', {"today": today_date})


def password(requset):
    return render("", 'home/password.html')


def book(requset):
    return render("", 'home/book.html')
