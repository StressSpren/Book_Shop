from django import forms
from apps.cart.models import Cart

class CartForm(forms.ModelForm):

    class Meta:

        model = Cart
        fields = []