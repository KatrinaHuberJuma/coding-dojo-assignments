# tv_shows_app APP LEVEL VIEWS
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Tv_show


def index(request):
    context = {
        "tv_shows": Tv_show.objects.all()
    }
    return render(request, "tv_shows_app/shows.html", context)


def create_show(request):
    if request.method == "POST":
        # pass the post data to the method we wrote and save the response in a variable called errors
        errors = Tv_show.objects.basic_validator(request.POST)      
        # check if the errors dictionary has anything in it
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/shows/new')
        else:
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
        # pass the post data to the method we wrote and save the response in a variable called errors
        errors = Tv_show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/shows/' + str(show_id) + '/edit')
        else:
            this_show = Tv_show.objects.get(id=show_id)
            this_show.title = request.POST["tv_show_title"]
            this_show.description = request.POST["tv_show_description"]
            this_show.network = request.POST["tv_show_network"]
            this_show.save()
            url = "/shows/" + str(show_id)
    return redirect(url)


def destroy_show(request, show_id):
    if request.method == "POST":
        this_show = Tv_show.objects.get(id=show_id)
        this_show.delete()
    return redirect("/shows")