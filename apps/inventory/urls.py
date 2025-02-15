from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.fetch_data, name="fetch_data"),
    path('book/<int:book_id>/', views.book_details, name='book_details'),
]
