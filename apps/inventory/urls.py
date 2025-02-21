from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('home/', views.fetch_data, name="fetch_data"),
    
    path('search/', views.search_books, name="search_books"),
    path('book/<int:book_id>/', views.book_details, name='book_details'),
]
