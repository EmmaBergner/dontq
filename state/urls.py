from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.ControlPage.as_view(), name="Control"),
]
