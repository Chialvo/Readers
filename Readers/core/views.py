from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from books.models import UserBook

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    user = request.user
    context = {
        'books_read':    UserBook.objects.filter(user=user, status='read').count(),
        'books_reading': UserBook.objects.filter(user=user, status='reading').count(),
        'books_want':    UserBook.objects.filter(user=user, status='want').count(),
        'following_count': user.following.count(),
        'current_books': UserBook.objects.filter(user=user, status='reading').select_related('book')[:6],
    }
    return render(request, 'core/home.html', context)