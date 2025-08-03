from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("index/",views.index),
    path("about/",views.about),
    path("team/",views.team),
    path("gallery/",views.gallery),
    path("services/",views.services),
    path("login/",views.login),
    path("register/",views.register),
    path("contact/",views.contact),
    
]

