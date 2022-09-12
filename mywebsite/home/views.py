from django.shortcuts import render
from datetime import date
import os

# Create your views here.


def today(requset):
    today_date = date.today()
    return render(requset, 'home/today.html', {"today_date": today_date})


def password(requset):
    random_password = os.urandom(8)
    return render(requset, 'home/password.html', {"random_password": random_password})


def book(requset):
    books = ["Pythons", "JavaScript", "HTML", "CSS"]
    return render(requset, 'home/book.html', {"books": books})
