from django.shortcuts import render
from .forms import BookForm
from apps.api.models import Books
from .models import Cart

# Create your views here.



def cart(request):

    cart = Cart.objects.all()
   


    return render(request, "cart.html", {'cart': cart})
