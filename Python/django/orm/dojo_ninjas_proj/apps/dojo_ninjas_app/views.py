# dojo_ninjas_app APP LEVEL VIEWS
from django.shortcuts import render, redirect

def index(request):
    return render(request, "dojo_ninjas_app/index.html")