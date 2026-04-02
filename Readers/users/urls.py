from django.urls import path
from .views import *

urlpatterns = [
    path('resgiter/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
]