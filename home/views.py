from django.shortcuts import render
import secrets


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def today(request):
    return render(request, 'home/today.html')


def random_password(request):
    password_length = 8
    password = secrets.token_urlsafe(password_length)
    return render(request, 'home/random_password.html', {'password': password})


def fav_books(request):
    books = ["The Hitchhiker's Guide to the Galaxy", "The Restaurant at the End of the Universe",
             "Life, the Universe and Everything", "So Long, and Thanks for All the Fish", "Mostly Harmless"]
    return render(request, 'home/fav_books.html', {'books': books})
