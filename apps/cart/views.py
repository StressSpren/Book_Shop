from django.shortcuts import render
from .forms import BookForm
from apps.api.models import Books

# Create your views here.



def cart(request):

    books = Books.objects.all()
   


    return render(request, "cart.html", {'books': books})
