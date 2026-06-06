from django.urls import path
from .views import *

urlpatterns = [
    path('', books, name='books'),
    path('<int:id>/', book_detail, name='book_detail'),
    path('<int:id>/star/', toggle_star, name='toggle_star'),
]