from django.urls import path

from . import views

urlpatterns = [
    path('getData', views.getData, name="getData"),
    path('addData', views.addData, name="addData"),


]