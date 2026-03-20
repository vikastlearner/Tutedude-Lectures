from . import views
from django.urls import path

urlpatterns = [
    path('app', views.index),
]