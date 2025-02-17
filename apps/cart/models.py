from django.db import models
from apps.api.models import Books
from apps.accounts.models import CustomUser

# Create your models here.

class Cart(models.Model):

    user_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Books,on_delete=models.SET_NULL, null = True)
    
    
    def __str__(self):
        return self.user_id.username