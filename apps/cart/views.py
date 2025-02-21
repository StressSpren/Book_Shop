from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import Cart_Deletion_Form
from .models import Cart

@login_required
def cart(request):
    """
    View to display the user's cart and handle cart item deletions.
    """
    # Fetch all cart items for the current user
    cart_items = Cart.objects.filter(user_id=request.user)

    # Calculate the total price of all items in the cart
    total_price = sum(item.book.price for item in cart_items)

    if request.method == "POST":
        form = Cart_Deletion_Form(request.POST)

        # Handle deletion of all cart items
        if "delete_cart" in request.POST:
            cart_items.delete()
            return redirect('cart')

        # Handle deletion of a specific cart item
        if "delete_item" in request.POST:
            cart_id = request.POST.get("cart_id")
            if cart_id:
                item = get_object_or_404(Cart, id=cart_id)
                item.delete()
                return redirect('cart')
    else:
        form = Cart_Deletion_Form()

    # Render the cart template with the cart items, form, and total price
    return render(request, "cart.html", {'cart': cart_items, 'form': form, 'total_price': total_price})