from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout

def home(request):
    return render(request, 'base/home.html')

def logout(request):
    auth_logout(request)
    return redirect('base/home.html')
