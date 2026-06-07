from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm, ProfileEditForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model

from books.models import UserBook

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

User = get_user_model()

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    is_following = request.user.is_authenticated and request.user.following.filter(id=user.id).exists()
    context = {
        'profile_user':  user,
        'is_following':  is_following,
        'followers_count': user.followers.count(),
        'following_count': user.following.count(),
        'books_read':    UserBook.objects.filter(user=user, status='read').select_related('book'),
        'books_reading': UserBook.objects.filter(user=user, status='reading').select_related('book'),
        'books_want':    UserBook.objects.filter(user=user, status='want').select_related('book'),
    }
    return render(request, 'users/profile.html', context)

def search_users(request):
    query = request.GET.get('q', '')
    if query:
        qs = User.objects.filter(username__icontains=query)
        if request.user.is_authenticated:
            qs = qs.exclude(id=request.user.id)
        results = qs
    else:
        results = []
    return render(request, 'users/search_users.html', {'results': results, 'query': query})

@login_required
def follow_user(request, username):
    target = get_object_or_404(User, username=username)
    if request.user.following.filter(id=target.id).exists():
        request.user.following.remove(target)
    else:
        request.user.following.add(target)
    return redirect('profile', username=username)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})