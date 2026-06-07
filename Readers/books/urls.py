from django.urls import path
from .views import *

urlpatterns = [
    path('', books, name='books'),
    path('<str:google_books_id>/', book_detail, name='book_detail'),
    path('<str:google_books_id>/status/', update_status, name='update_status'),
]