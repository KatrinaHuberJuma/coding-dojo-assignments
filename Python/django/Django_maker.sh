#!/bin/bash

# Use $1 to get the first argument:

chmod u+x Django_maker.sh 

# echo Hello, is this a new project y/n?
# read new_proj


echo what would you like to name your project?
read project_name
django-admin startproject $project_name

cd $project_name

touch README.txt

mkdir apps



echo Would you like to add an app y/n?
read make_app

while [[ "$make_app" = "y" ]]; 
do
	echo Hello, what would you like to name your app?
	read app_name




	cd apps
	python ../manage.py startapp $app_name

	cd $app_name
	touch urls.py
	mkdir templates/ templates/$app_name
	touch templates/$app_name/index.html
	mkdir static/ static/$app_name
	mkdir static/$app_name/css/ static/$app_name/js/ static/$app_name/images/ 

	cd ../../


	echo -e  "TODO in $project_name/$project_name/: 
	\n _____________ in $project_name/settings.py,  INSTALLED_APPS list 
	\n __________________________'apps.${app_name}', 
	\n _____________ in urls.py:  
	\n __________________________ comment out, or just delete 'from django.contrib import admin'
	\n __________________________url(r'^', include('apps.${app_name}.urls')),	# add to url patterns, don't forget the comma 
	TODO in $project_name/apps$app_name/: 
	\n _____________ in urls.py:
	\n __________________________ from django.conf.urls import url
	\n __________________________ from . import views
	\n __________________________in urlpatterns add
	\n ________________________________________ url(r'^$', views.index), # index is the name of a method in views.py
	\n _____________ in views.py:
	\n __________________________from django.shortcuts import render, redirect
	\n __________________________def index(request):
	\n __________________________    return render(request, '$app_name/index.html')" >> README.txt

	echo Would you like to add an app y/n?
	read make_app

done

