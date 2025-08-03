from django.urls import path
from . import views

urlpatterns=[
  path("dashboard/", views.dashboard),
  path("lectures/",views.lectures),
  path("enotes/",views.enotes),
  path("mytask/",views.task),
  path("profile/", views.profile),
  path("category/",views.mycategory),
  path("signout/",views.signout),
  path("softkit/",views.softkit),
  path("lecturecat/",views.lecturecat),
  

  
  ]