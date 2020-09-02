from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("edit", views.edit, name="edit"),
    path("randompage",views.randompage, name="randompage"),
    path("<str:name>", views.checkentry, name="checkentry")
]
