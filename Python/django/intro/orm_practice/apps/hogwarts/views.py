# hogwarts APP LEVEL VIEWS
from django.shortcuts import render, redirect
def index(request):
    return render(request, "hogwarts/index.html")