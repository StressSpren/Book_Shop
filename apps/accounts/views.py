# accounts/views.py
# from django.contrib.auth.forms import UserCreationForm

""" Not sure what these do """
from django.urls import reverse_lazy 
from django.views.generic import CreateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@login_required
def profile_page_view(request):
    return render(request, 'profile_page.html')


    