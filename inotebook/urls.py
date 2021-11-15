from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path("createNotes/",views.createNotes,name="createNotes"),
    path("updateNotes/<int:pk>/",views.updateNotes,name="updateNotes"),
    path("deleteNotes/<int:pk>",views.deleteNotes,name="deleteNotes"),
]
