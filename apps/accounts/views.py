# accounts/views.py
# from django.contrib.auth.forms import UserCreationForm

""" Not sure what these do """
from django.urls import reverse_lazy 
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages


from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@login_required
def profile_page_view(request):
    if request.method == "POST":
        user = request.user
        user.delete()  # Deletes the user from the database
        logout(request)  # Logs the user out after deletion
        messages.success(request, "Your account has been deleted.")
        return redirect("home")  # Redirect to the homepage or another page
     
    return render(request, 'profile_page.html')


    