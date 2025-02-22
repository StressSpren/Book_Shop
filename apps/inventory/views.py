# Import necessary Django and Python modules
from django.shortcuts import render, redirect
import requests
from .forms import CartForm
from django.contrib.auth.decorators import login_required
from apps.api.models import Books, Category, Author
from apps.cart.models import Cart
from apps.accounts.models import CustomUser

@login_required  # Ensures user must be logged in to access this view
def fetch_data(request):
    """
    View to fetch and display all books categorized by their category.
    Also handles adding books to cart via POST request.
    """
    # Create a list of QuerySets, each containing books filtered by category
    data_list = [Books.objects.filter(category=c) for c in Category.objects.all()]

    # Handle POST request for adding book to cart
    if request.method == "POST" and "id_output" in request.POST:
        form = CartForm(request.POST)
        if form.is_valid():
            cart_field = form.save(commit=False)  # Create cart object but don't save yet
            cart_field.user_id = request.user     # Assign current user
            cart_field.book = Books.objects.get(id=request.POST.get("id_output"))  # Get book by ID
            cart_field.save()  # Save cart entry to database
            return redirect('cart')  # Redirect to cart page after successful addition
    else:
        form = CartForm()  # Create empty form for GET requests

    # Render template with book data, categories, and cart form
    return render(request, 'index.html', {'data_list': data_list, 'cat': Category.objects.all(), 'form': form})


@login_required
def book_details(request, book_id):
    """
    View to display detailed information about a specific book.
    Fetches book details, author info, and category info from API.
    Also handles adding book to cart via POST request.
    """
    # Construct API URL for specific book
    url = f"https://bookshop-2ucx.onrender.com/api/books/{book_id}"

    try:
        # Fetch book data from API
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad HTTP responses
        books = response.json()

        # Fetch author details from API
        author_response = requests.get(books.get('author'))
        author_data = author_response.json()
        # Update books dict with author information
        books.update({
            'author_first': author_data.get('first_name'),
            'author_last': author_data.get('last_name'),
            'author_pic': author_data.get('profile_picture'),
            'author_bio': author_data.get('bio')
        })

        # Fetch category details from API
        category_response = requests.get(books.get('category'))
        cat_data = category_response.json()
        books['category_name'] = cat_data.get('name')

    except requests.exceptions.RequestException as e:
        # Handle any API request errors
        print(f"Error fetching data: {e}")
        books = {}

    # Handle POST request for adding book to cart
    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            cart_field = form.save(commit=False)
            cart_field.user_id = request.user
            cart_field.book = Books.objects.get(id=book_id)
            cart_field.save()
            return redirect('cart')  # Redirect to cart page after successful addition
    else:
        form = CartForm()  # Create empty form for GET requests

    # Render template with book details and cart form
    return render(request, 'book_details.html', {'data': books, 'form': form})


@login_required
def search_books(request):
    """
    View to handle book search functionality.
    Fetches all books from API and filters based on search keyword.
    """
    # API endpoint for books
    url = "https://bookshop-2ucx.onrender.com/api/books"

    try:
        # Fetch all books from API
        response = requests.get(url)
        response.raise_for_status()
        books = response.json().get('results', [])  # Get results or empty list if none
    except requests.exceptions.RequestException as e:
        # Handle API request errors
        print(f"Error fetching data: {e}")
        books = []

    # Filter books based on search keyword (only for POST requests)
    title_matches = [book for book in books if request.method == "POST" and request.POST.get("keyword", "").lower() in book['title'].lower()]
   
        


        

    # Render template with search results
    return render(request, "search.html", {"book_title": title_matches})




def home_view(request):

    books = Books.objects.all()
    categories = Category.objects.all() # Fetch all categories from database
    authors = Author.objects.all() # Fetch all authors from database
    cart = Cart.objects.all()
    
    

    if request.method == "POST" and "id_output" in request.POST:
        form = CartForm(request.POST)
        if form.is_valid():
            cart_field = form.save(commit=False)  # Create cart object but don't save yet
            cart_field.user_id = request.user     # Assign current user
            cart_field.book = Books.objects.get(id=request.POST.get("id_output"))  # Get book by ID
            cart_field.save()  # Save cart entry to database
            return redirect('cart')
    else:
        form = CartForm()  # Create empty form for GET requests


    return render(request, 'home.html', {'books': books, 'categories': categories, 'authors': authors, 'cart': cart, 'form': form})