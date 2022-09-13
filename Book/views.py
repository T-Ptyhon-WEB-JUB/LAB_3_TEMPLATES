from django.shortcuts import render


def fav_books(request):
    books = ["Renad on the moon", "Renamd Monster Hunter", "Renamd Adventures"]
    return render(request, "books.html", context={"books": books})
