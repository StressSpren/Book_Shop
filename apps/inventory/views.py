from django.shortcuts import render, redirect
import requests
from .forms import CartForm
from apps.cart.models import Cart
from django.contrib.auth.decorators import login_required
from apps.api.models import Books
from apps.accounts.models import CustomUser

# Create your views here.

def fetch_data(request):

    url = "http://127.0.0.1:8000/api/books"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        books = data.get('results', [])

        for book in books:
            author_url = book.get('author')  # Get the URL of the author
            if author_url:  # If there's a URL, fetch the author's details
                author_response = requests.get(author_url)
                if author_response.status_code == 200:
                    author_data = author_response.json()
                    book['author_name'] = author_data.get('first_name')
                    book['author_last'] = author_data.get('last_name')

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        books = []  # Fallback to empty list in case of error

    return render(request, 'index.html', {'data': books})

@login_required
def book_details(request, book_id):

    url = f"http://127.0.0.1:8000/api/books/{book_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        books = data


        # Author Allocation
        author_url = books.get('author')
        author_response = requests.get(author_url)
        author_data = author_response.json()
        books['author_first'] = author_data.get('first_name')
        books['author_last'] = author_data.get('last_name')
        books['author_pic'] = author_data.get('profile_picture')
        books['author_bio'] = author_data.get('bio')


    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        books = []  # Fallback to empty list in case of error

    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            cart_item = form.save(commit=False)
            cart_item.user_id = CustomUser.objects.get(id=f"{request.user.id}")
            cart_item.book = Books.objects.get(id=book_id)
            cart_item.save()
            return redirect('cart')

    else:
        form = CartForm()

    return render(request, 'book_details.html', {'data': books, 'form': form})


def search_books(request):
    url = f"http://127.0.0.1:8000/api/books"

     
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    books = data.get('results', [])
    dict_book = {"matches": []}

    if request.method == "POST":  
        keyword = request.POST.get("keyword", "").lower()  # Get user input
        for book in books:
            if keyword in book['title'].lower():
                dict_book["matches"].append(book)

        # Render results page with matching books
    return render(request, "search.html", {"books": dict_book["matches"]})


