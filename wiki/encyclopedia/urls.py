from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.checkentry, name="checkentry")
    #path("search", views.search, name="search")
]
