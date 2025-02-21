from django.shortcuts import render, redirect
import requests
from .forms import CartForm
from django.contrib.auth.decorators import login_required
from apps.api.models import Books, Category
from apps.accounts.models import CustomUser
from apps.cart.models import Cart


# Create your views here.
@login_required
def fetch_data(request):

    count = 1
    data_list = []
    cat = Category.objects.all()
    for c in cat:
        book = Books.objects.filter(category=Category(id=count))
        data_list.append(book)
        count += 1

    
    if "id_output" in request.POST:
        form = CartForm(request.POST)
        cart_id = request.POST.get("id_output")
        if form.is_valid():
            cart_field = form.save(commit=False)
            cart_field.user_id = CustomUser.objects.get(id=f"{request.user.id}")
            cart_field.book = Books.objects.get(id=cart_id)
            cart_field.save()
            
    else:
        form = CartForm()

    return render(request, 'index.html', {'data_list': data_list, 'cat': cat, 'form': form})

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

        # Data
        books['author_first'] = author_data.get('first_name')
        books['author_last'] = author_data.get('last_name')
        books['author_pic'] = author_data.get('profile_picture')
        books['author_bio'] = author_data.get('bio')

        # Category Allocation
        category_url = books.get('category')
        category_response = requests.get(category_url)
        cat_data = category_response.json()
        
        # Data
        books['category_name'] = cat_data.get('name')


    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        books = []  # Fallback to empty list in case of error

    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            cart_field = form.save(commit=False)
            cart_field.user_id = CustomUser.objects.get(id=f"{request.user.id}")
            cart_field.book = Books.objects.get(id=book_id)
            cart_field.save()
            return redirect('cart')

    else:
        form = CartForm()

    return render(request, 'book_details.html', {'data': books, 'form': form})

@login_required
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


