from django.shortcuts import render
from django.http import HttpRequest
from datetime import date
import random
import string

# Create your views here.


def home(requset: HttpRequest):
    return render(requset, 'home/index.html')


def today(requset: HttpRequest):
    today_date = date.today()
    return render(requset, 'home/today.html', {"today_date": today_date})

# differents ways to get the password


def password(requset: HttpRequest):
    # 1- random_password = random.randrange(0, 100000000, 8)

    # 2-
    random_password = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=8))

    # 3- random_password = random.choices(['3', '4', '5', '6', '7', '8', '9', 'a', 'b'], k=8)

    # 4-
    # import secrets
    # password_length = 13
    # print(secrets.token_urlsafe(password_length))

    # 5-
    # import random
    # data = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    # def Getpass(data):
    #              Max = 12
    #              password = ""
    #              while len(password) != Max:
    #                  Val = random.choice(data)
    #                  password += Val
    #              return password

    return render(requset, 'home/password.html', {"random_password": random_password})


def book(requset: HttpRequest):
    books = ["Pythons", "JavaScript", "HTML", "CSS"]
    return render(requset, 'home/book.html', {"books": books})
