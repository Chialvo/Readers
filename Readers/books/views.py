from django.shortcuts import render, get_object_or_404
from .models import *

def books(request):
    items = Book.objects.all()
    return render(request, "books/books.html", {"books": items})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/book_detail.html',  {'book': book})
