# login_app APP LEVEL VIEWS
from django.shortcuts import render, redirect
def index(request):
    return render(request, "login_app/index.html")

