from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book, UserBook, Genre
from .services import search_books, get_book_detail
from django.utils import timezone
from django.db.models import Avg, Count

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

def save_genres(book, genres):
    for genre_name in genres:
        # Tomar solo el primer nivel: "Juvenile Fiction / Fantasy" → "Juvenile Fiction"
        clean_name = genre_name.split('/')[0].strip()
        genre, _ = Genre.objects.get_or_create(name=clean_name)
        book.genres.add(genre)

@login_required
def update_status(request, google_books_id):
    if request.method != 'POST':
        return redirect('book_detail', google_books_id=google_books_id)

    data_api = get_book_detail(google_books_id)
    book, created = Book.objects.get_or_create(
        google_books_id=google_books_id,
        defaults={'title': data_api['title'], 'author': data_api['author'], 'cover_url': data_api['cover_url']}
    )

    # Guardar géneros si es la primera vez
    if created or not book.genres.exists():
        save_genres(book, data_api.get('genres', []))

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
        read_date  = timezone.now().date()
    else:
        rating_val = None
        read_date  = None

    UserBook.objects.update_or_create(
        user=request.user,
        book=book,
        defaults={'status': status, 'rating': rating_val, 'read_date': read_date}
    )
    return redirect('book_detail', google_books_id=google_books_id)


@login_required
def library(request):
    user = request.user
    current_year = timezone.now().year

    books_read    = UserBook.objects.filter(user=user, status='read').select_related('book')
    books_reading = UserBook.objects.filter(user=user, status='reading').select_related('book')
    books_want    = UserBook.objects.filter(user=user, status='want').select_related('book')

    read_this_year = books_read.filter(read_date__year=current_year).count()

    avg_rating = books_read.aggregate(avg=Avg('rating'))['avg']
    avg_rating = round(avg_rating, 1) if avg_rating else None

    top_genres = Genre.objects.filter(
        book__user_books__user=user,
        book__user_books__status='read'
    ).annotate(count=Count('id')).order_by('-count')[:5]

    best_rated = books_read.order_by('-rating').first()

    context = {
        'books_read':      books_read,
        'books_reading':   books_reading,
        'books_want':      books_want,
        'read_this_year':  read_this_year,
        'avg_rating':      avg_rating,
        'top_genres':      top_genres,
        'best_rated':      best_rated,
        'current_year':    current_year,
    }
    return render(request, 'books/library.html', context)