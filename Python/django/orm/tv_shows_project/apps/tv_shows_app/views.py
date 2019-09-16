# tv_shows_app APP LEVEL VIEWS
from django.shortcuts import render, redirect
from .models import Tv_show


def index(request):
    context = {
        "tv_shows": Tv_show.objects.all()
    }
    return render(request, "tv_shows_app/shows.html", context)


def create_show(request):
    if request.method == "POST":
        title = request.POST["tv_show_title"]
        # TODO network = request.POST["show_network"]
        description = request.POST["tv_show_description"]
        Tv_show.objects.create(title=title, description=description)
        return redirect("/shows")


def new_show(request):
    return render(request, "tv_shows_app/new_show.html")


def one_show(request, show_id):
    context = {
        "show": Tv_show.objects.get(id=show_id)
    }
    return render(request, "tv_shows_app/show.html", context)

def edit_show(request, show_id):
    context = {
        "show": Tv_show.objects.get(id=show_id)
    }
    return render(request, "tv_shows_app/edit_show.html", context)


def update_show(request, show_id):
    if request.method == "POST":
        this_show = Tv_show.objects.get(id=show_id)
        this_show.title = request.POST["tv_show_title"]
        this_show.description = request.POST["tv_show_description"]
        this_show.network = request.POST["tv_show_network"]
        this_show.save()
        # url = "shows/" + str(show_id)
        # print(url)

    return redirect("/shows")


def destroy_show(request, show_id):
    if request.method == "POST":
        this_show = Tv_show.objects.get(id=show_id)
        print(this_show)
        print(this_show.delete())
    return redirect("/shows")