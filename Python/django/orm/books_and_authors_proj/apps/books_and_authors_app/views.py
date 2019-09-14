from django.shortcuts import render, redirect

# Create your views here.
# books_and_authors_app APP LEVEL VIEWS

def index(request):
    return render(request, "books_and_authors_app/index.html")