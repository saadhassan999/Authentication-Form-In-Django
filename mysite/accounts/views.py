from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
# Create your views here.
def Register_view(response):

    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Register Successfully</h1>")
    else:
        form = RegisterForm()
    return render(response, "accounts/register.html", {'form' : form})