from django.shortcuts import render, redirect
from .forms import BookForm, Cart_Deletion_Form
from .models import Cart
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def cart(request):

    cart_all = Cart.objects.all()
    cart_item = Cart.objects.filter(user_id=request.user)

    if request.method == "POST":
        form = Cart_Deletion_Form(request.POST)

        if "delete_cart" in request.POST:
            cart_item.delete()
            return redirect('cart')
        
        if "delete_item" in request.POST:
            cart_id = request.POST.get("cart_id")
            if cart_id:
                item = Cart.objects.get(id=cart_id)
                item.delete()
                return redirect('cart')

    else:
        form = Cart_Deletion_Form()

    return render(request, "cart.html", {'cart_item': cart_item, 'cart': cart_all, 'form': form})
