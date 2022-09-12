from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from datetime import date
import secrets
# Create your views here.
def today(request):
    today = date.today()
    return render(request, 'thamerLab3/index.html', {'today': today})

def password(request):
    passLen = 12
    return render(request, 'password/pass.html', {'pass' : secrets.token_urlsafe(passLen)})
    """_summary_
    """
def books(request):
    book = ['thamer', 'ali', 'abduallh']
    return render(request, 'books/books.html', {'book': book})
