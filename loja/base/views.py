from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def home(request):
    return render(request, "base/home.html")


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("base:success")
    else:
        form = UserRegistrationForm()
    return render(request, "registration/register.html", {"form": form})


def success(request):
    return render(request, "registration/success.html")
