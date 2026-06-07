from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book, UserBook
from .services import search_books, get_book_detail

def books(request):
    query = request.GET.get('q', '')
    results = search_books(query) if query else []
    return render(request, 'books/books.html', {'results': results, 'query': query})

def book_detail(request, google_books_id):
    data = get_book_detail(google_books_id)
    book, _ = Book.objects.get_or_create(
        google_books_id=google_books_id,
        defaults={'title': data['title'], 'author': data['author'], 'cover_url': data['cover_url']}
    )
    user_book = None
    if request.user.is_authenticated:
        user_book = UserBook.objects.filter(user=request.user, book=book).first()
    return render(request, 'books/book_detail.html', {
        'book': book,
        'data': data,
        'user_book': user_book,
    })

@login_required
def update_status(request, google_books_id):
    if request.method != 'POST':
        return redirect('book_detail', google_books_id=google_books_id)

    data_api = get_book_detail(google_books_id)
    book, _ = Book.objects.get_or_create(
        google_books_id=google_books_id,
        defaults={'title': data_api['title'], 'author': data_api['author'], 'cover_url': data_api['cover_url']}
    )

    status = request.POST.get('status')
    rating = request.POST.get('rating')

    if status == 'remove':
        UserBook.objects.filter(user=request.user, book=book).delete()
        return redirect('book_detail', google_books_id=google_books_id)

    if status not in ('want', 'reading', 'read'):
        return redirect('book_detail', google_books_id=google_books_id)

    if status == 'read':
        if not rating or not rating.isdigit() or not (1 <= int(rating) <= 5):
            return redirect('book_detail', google_books_id=google_books_id)
        rating_val = int(rating)
    else:
        rating_val = None

    UserBook.objects.update_or_create(
        user=request.user,
        book=book,
        defaults={'status': status, 'rating': rating_val}
    )
    return redirect('book_detail', google_books_id=google_books_id)