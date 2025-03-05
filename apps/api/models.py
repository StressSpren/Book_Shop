from django.db import models
from django.core.exceptions import ValidationError

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
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    cover_image = models.ImageField(upload_to='book_pics/', blank=True, null=True)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def clean(self):
        if self.price < 0:
            raise ValidationError("Price cannot be negative.")
        if self.stock < 0:
            raise ValidationError("Stock cannot be negative.")

    def __str__(self):
        return self.title