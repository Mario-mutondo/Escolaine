from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render (
        request, "accounts/login.html",
    )

def register(request):
    return render (
        request, "accounts/register.html",
    )