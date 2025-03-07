# Import necessary Django and Python modules
from django.shortcuts import render, redirect
import requests
from .forms import CartForm
from django.contrib.auth.decorators import login_required
from apps.api.models import Books, Category, Author
from apps.cart.models import Cart
from apps.accounts.models import CustomUser as User
import math

@login_required  # Ensures user must be logged in to access this view
def genres(request):
    """
    View to fetch and display all books categorized by their category.
    Also handles adding books to cart via POST request.
    """
    # Create a list of QuerySets, each containing books filtered by category
    data_list = [Books.objects.filter(category=c) for c in Category.objects.all()]

    # Handle POST request for adding book to cart
    if request.method == "POST" and "id_output" in request.POST:
        form = CartForm(request.POST)
        book = Books.objects.get(id=request.POST.get("id_output"))
        if form.is_valid():
            cart_field = form.save(commit=False)  # Create cart object but don't save yet
            cart_field.user_id = request.user     # Assign current user
            cart_field.book = Books.objects.get(id=request.POST.get("id_output"))  # Get book by ID
            cart_field.save()  # Save cart entry to database

             # Decrease the stock count
            if book.stock == 0:
                return redirect('fetch_data')
            book.stock -= 1
            book.save()
            return redirect('cart')  # Redirect to cart page after successful addition
    else:
        form = CartForm()  # Create empty form for GET requests

    # Render template with book data, categories, and cart form
    return render(request, 'genres.html', {'data_list': data_list, 'cat': Category.objects.all(), 'form': form})


@login_required
def book_details(request, book_id):
  
    book = Books.objects.get(id=book_id)  # Fetch book by ID

    base_author = book.author.id  # Get author ID from book data
    author = Author.objects.get(id=base_author)

    # Handle POST request for adding book to cart
    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            cart_field = form.save(commit=False)
            cart_field.user_id = request.user
            cart_field.book = Books.objects.get(id=book_id)
            cart_field.save()

             # Decrease the stock count
            book.stock -= 1
            book.save()

            return redirect('cart')  # Redirect to cart page after successful addition
    else:
        form = CartForm()  # Create empty form for GET requests

    # Render template with book details and cart form
    return render(request, 'book_details.html', {'data': book, 'form': form, 'author': author})


@login_required
def search_books(request):

    books = Books.objects.all()  # Fetch all books from database
    book_list = []

    if request.method == "POST" and 'keyword' in request.POST:
        keyword = request.POST.get('keyword')
        for book in books:
            if keyword.lower() in book.title.lower():
                book_list.append(book)
            if keyword == book.isbn:
                book_list.append(book)

    # Render template with search results
    return render(request, "search.html", {"book_title": book_list})


# @login_required
# Including @login_requried here gets in the way of image retrieval and creation, comment out when adding and re-enable when going live. 
def home_view(request):

    books = Books.objects.all()
    categories = Category.objects.all() # Fetch all categories from database
    authors = Author.objects.all() # Fetch all authors from database
    cart = Cart.objects.all()

    if request.method == "POST" and "id_output" in request.POST:
        form = CartForm(request.POST)
        if form.is_valid():
            book = Books.objects.get(id=request.POST.get("id_output"))
            user = User.objects.get(id=request.user.id)
            if book.stock == 0:
                return redirect('home')
            cart_field = form.save(commit=False)  # Create cart object but don't save yet
            cart_field.user_id = user     # Assign current user
            cart_field.book = Books.objects.get(id=request.POST.get("id_output"))  # Get book by ID
            cart_field.save()  # Save cart entry to database

             # Decrease the stock count
            book.stock -= 1
            book.save()
            return redirect(request.META.get('HTTP_REFERER', 'home'))
    else:
        form = CartForm()  # Create empty form for GET requests


    return render(request, 'home.html', {'books': books, 'categories': categories, 'authors': authors, 'cart': cart, 'form': form})