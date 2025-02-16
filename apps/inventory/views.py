from django.shortcuts import render
import requests

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


def book_details(request, book_id):

    url = f"http://127.0.0.1:8000/api/books/{book_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        books = data

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

    return render(request, 'book_details.html', {'data': books})

