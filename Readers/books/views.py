from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book

def books(request):
    all_books = Book.objects.all()
    return render(request, 'books/books.html', {'books': all_books})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    is_starred = request.user.is_authenticated and book.starred_by.filter(id=request.user.id).exists()
    return render(request, 'books/book_detail.html', {'book': book, 'is_starred': is_starred})

@login_required
def toggle_star(request, id):
    book = get_object_or_404(Book, id=id)
    if book.starred_by.filter(id=request.user.id).exists():
        book.starred_by.remove(request.user)
    else:
        book.starred_by.add(request.user)
    return redirect('book_detail', id=id)