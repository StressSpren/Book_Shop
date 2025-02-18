from django import  forms
from apps.api.models import Books
from .models import Cart
class BookForm(forms.ModelForm):
    class Meta:
        model= Books
        fields = '__all__'

class Cart_Deletion_Form(forms.ModelForm):
    class Meta:
        model= Cart
        fields = '__all__'