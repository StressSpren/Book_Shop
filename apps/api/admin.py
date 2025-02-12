from django.contrib import admin
from .models import Books, Author, Category

# Register your models here.
admin.site.register(Books)
admin.site.register(Author)
admin.site.register(Category)