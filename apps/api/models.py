from django.db import models
from django.core.exceptions import ValidationError
from decimal import Decimal

# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Author Model
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='authors/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Books(models.Model):

    class Meta:
        verbose_name_plural = 'Books'
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="books")
    description = models.TextField()
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    cover_image = models.ImageField(upload_to='book_pics/', blank=True, null=True)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    for_sale = models.BooleanField(default=False, null=True, blank=True)

    def save(self, *args, **kwargs):

        # Apply discount when for_sale is first set to True
        if self.for_sale and self.price == self.original_price:
            self.price = self.original_price * Decimal('0.8')
        
        # Add item to sale when above 60 stock
        if self.stock > 60 and not self.for_sale:
            self.for_sale = True
            

        # Remove discount when stock is less than 10 and change for_sale to False
        if self.for_sale and self.stock < 10 and self.price != self.original_price:
            self.for_sale = False
            self.price = self.original_price
        
        super().save(*args, **kwargs)

    def clean(self):
        if self.price < 0:
            raise ValidationError("Price cannot be negative.")
        if self.stock < 0:
            raise ValidationError("Stock cannot be negative.")

    def __str__(self):
        return self.title