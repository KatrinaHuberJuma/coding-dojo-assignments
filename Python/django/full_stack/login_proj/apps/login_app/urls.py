# login_app APP LEVEL URLS
from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^users$', views.root),
    url(r'^users/login$', views.login),
    url(r'^users/new$', views.reg),
    url(r'^users/success$', views.success),
    url(r'^users/logout$', views.logout),
]
