from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book
from .services import search_books, get_book_detail

def books(request):
    query = request.GET.get("q", "")
    results = search_books(query) if query else []
    return render(request, "books/books.html", {"results": results, "query": query})

def book_detail(request, google_books_id):
    data = get_book_detail(google_books_id)
    # Si ya está en la BD lo traemos, si no lo creamos al vuelo
    book, _ = Book.objects.get_or_create(
        google_books_id=google_books_id,
        defaults={"title": data["title"], "author": data["author"], "cover_url": data["cover_url"]}
    )
    is_starred = request.user.is_authenticated and book.starred_by.filter(id=request.user.id).exists()
    return render(request, "books/book_detail.html", {"book": book, "data": data, "is_starred": is_starred})

@login_required
def toggle_star(request, google_books_id):
    data = get_book_detail(google_books_id)
    book, _ = Book.objects.get_or_create(
        google_books_id=google_books_id,
        defaults={"title": data["title"], "author": data["author"], "cover_url": data["cover_url"]}
    )
    if book.starred_by.filter(id=request.user.id).exists():
        book.starred_by.remove(request.user)
    else:
        book.starred_by.add(request.user)
    return redirect("book_detail", google_books_id=google_books_id)