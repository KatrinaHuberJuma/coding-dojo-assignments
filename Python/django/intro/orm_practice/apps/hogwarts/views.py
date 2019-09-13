# hogwarts APP LEVEL VIEWS
from django.shortcuts import render, redirect
from .models import Hogwarts


def index(request):
    context = {
        "all_students": Hogwarts.objects.all()
    }
    # print(context["all_students"])
    return render(request, "hogwarts/index.html", context)