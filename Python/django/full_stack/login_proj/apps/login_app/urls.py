# login_app APP LEVEL URLS
from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
]
