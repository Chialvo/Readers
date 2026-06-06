from django.urls import path
from .views import *

urlpatterns = [
    path("", books, name="books"),
    path("<str:google_books_id>/", book_detail, name="book_detail"),
    path("<str:google_books_id>/star/", toggle_star, name="toggle_star"),
]