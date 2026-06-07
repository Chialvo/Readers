from django.urls import path
from .views import *

urlpatterns = [
    path('profile/<str:username>/', profile_view, name='profile'),
    path('search/', search_users, name='search_users'),
    path('follow/<str:username>/', follow_user, name='follow_user'),
    path('edit/', edit_profile, name='edit_profile'),
]