from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        return redirect('profile', username=request.user.username)
    return render(request, 'core/landing.html')  # o el login