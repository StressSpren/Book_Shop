from django import  forms
from apps.api.models import Books

class BookForm(forms.ModelForm):
    class Meta:
        model= Books
        fields = '__all__'