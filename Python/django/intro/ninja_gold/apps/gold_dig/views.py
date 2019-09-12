
# Create your views here.
from django.shortcuts import render, redirect 
import random

def index(request):
    if "gold" not in request.session:
        request.session['gold'] = 0
    print(request.session['gold'])
    return render(request, "gold_dig/index.html")

def process_money(request):
    # if request.method == "GET":
    #     print("a GET request is being made to this route")
    #     return render(request, "gold_dig/index.html")
    if request.method == "POST":
        if request.POST['location'] == 'farm':
            request.session['gold'] += random.choice([10, 15, 20])
        elif request.POST['location'] == 'cave':
            request.session['gold'] += random.choice([5, 10])
        elif request.POST['location'] == 'house':
            request.session['gold'] += random.choice([2, 3, 4, 5])
        else:
            request.session['gold'] += random.choice([20, -20])
        return redirect("/")


def clear_session(request):
    request.session.clear()
    return redirect("/")
