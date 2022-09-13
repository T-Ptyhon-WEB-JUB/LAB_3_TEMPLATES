from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string
from datetime import datetime
# Create your views here.
def tody(request : HttpRequest):
    t = datetime.now()
    return render(request, 'Home/today.html', {"today": t})
def pas(request : HttpRequest):
    random_password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return render(request, 'Home/password.html', {"pas": random_password})

def home(request):
    return render(request, "Home/home.html", context={})
