from django.shortcuts import render
from datetime import date
import random
import string

# Create your views here.


def home(requset):
    return render(requset, 'home/index.html')


def today(requset):
    today_date = date.today()
    return render(requset, 'home/today.html', {"today_date": today_date})


def password(requset):
    # random_password = random.randrange(0, 100000000, 8)
    random_password = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=8))

    return render(requset, 'home/password.html', {"random_password": random_password})


def book(requset):
    books = ["Pythons", "JavaScript", "HTML", "CSS"]
    return render(requset, 'home/book.html', {"books": books})
