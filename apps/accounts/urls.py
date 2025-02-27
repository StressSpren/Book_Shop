
from .views import SignUpView
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile_page/", views.profile_page_view, name="profile"),
   
]
