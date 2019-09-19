
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User


def root(request):
    print(User.objects.all())
    return render(request, "login_app/index.html")

def login(request):
    errors = {}
    if request.method == "POST":
        possible_user = User.objects.filter(email=request.POST["email"])
        try:
            this_user = possible_user[0]
            if request.POST["password"] == this_user.hashed_pw:
                return redirect("/users/success")
            errors['password_oopsie_error']= "You seem to have forgotten your password. Too bad for you, we for sure don't save your plaintext password so get a new email and come back."
        except IndexError:
            errors['email_oopsie_error']=  "No user exists with this email, go ahead and register!"
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        
    return redirect("/users")

def reg(request):
    if request.method == "POST":
        # pass the post data to the method we wrote and save the response in a variable called errors
        errors = User.objects.basic_validator(request.POST) 
        if request.POST["password"] != request.POST["confirm_password"]:
            errors['pw_confrimation_fail'] = "Password does not match confirmation password"     
        # check if the errors dictionary has anything in it
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/users')
        else:
            password = request.POST["confirm_password"]
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            birthday = request.POST["birthday"]
            User.objects.create(first_name=first_name, last_name=last_name, email=email, hashed_pw=password, birthday=birthday)
    return redirect("/users/success")

def success(request):
    
    return render(request, "login_app/success.html")