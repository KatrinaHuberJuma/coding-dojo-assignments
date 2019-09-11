from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new), 
    url(r'^blogs$', views.display),
    url(r'^create$', views.create),  
    url(r'^(?P<blog_id>[0-9])$', views.show),  
    url(r'^(?P<blog_id>[0-9]+)/edit$', views.edit),  
    url(r'^(?P<blog_id>[0-9]+)/destroy$', views.destroy),  
]                           # r'^$' - 
                                # the rest of the route both starts and ends with nothing 
                                # (i.e. "/" is the full route), and
                            # views.index - 
                                # if the requested route matches this pattern, 
                                # then the function with the name "index" from 
                                # this app's views.py file will be invoked.
                            # Note: ALL route patterns at the app level should end with $.