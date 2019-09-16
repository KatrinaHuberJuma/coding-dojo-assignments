# tv_shows_app APP LEVEL URLS
from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^shows$', views.index),
    url(r'^shows/new$', views.new_show),
    url(r'^shows/create$', views.create_show),
    url(r'^shows/(?P<show_id>\d+)$', views.one_show),
    url(r'^shows/(?P<show_id>\d+)/edit$', views.edit_show),
    url(r'^shows/(?P<show_id>\d+)/update$', views.update_show),
    url(r'^shows/(?P<show_id>\d+)/destroy$', views.destroy_show),
]

