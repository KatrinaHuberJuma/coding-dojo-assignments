TODO in fav_books_proj/fav_books_proj/: 
	
 _____________ in fav_books_proj/settings.py,  INSTALLED_APPS list 
	
 *__________________________'apps.fav_books_app', 
	
 _____________ in urls.py:  
	
 *__________________________ comment out, or just delete 'from django.contrib import admin'
	
 *__________________________url(r'^', include('apps.fav_books_app.urls')),	# add to url patterns, don't forget the comma 
	TODO in fav_books_proj/appsfav_books_app/: 
	
 _____________ in urls.py:
	
 *__________________________ from django.conf.urls import url
	
 *__________________________ from . import views
	
 *__________________________in urlpatterns add
	
 *________________________________________ url(r'^$', views.index), # index is the name of a method in views.py
	
 _____________ in views.py:
	
 *__________________________from django.shortcuts import render, redirect
	
 *__________________________def index(request):
	
 *__________________________    return render(request, 'fav_books_app/index.html')
