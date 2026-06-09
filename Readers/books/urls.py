from django.urls import path
from .views import *

urlpatterns = [
    path('', books, name='books'),
    path('biblioteca/', library, name='library'),
    path('<str:google_books_id>/', book_detail, name='book_detail'),
    path('<str:google_books_id>/status/', update_status, name='update_status'),
]