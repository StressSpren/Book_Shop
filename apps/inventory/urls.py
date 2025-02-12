from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.fetch_data, name="fetch_data"),
]
