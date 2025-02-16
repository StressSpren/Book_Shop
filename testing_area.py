import requests


url = f"http://127.0.0.1:8000/api/books"
response = requests.get(url)
response.raise_for_status()
data = response.json()
books = data.get('results', [])
print(books)
keyword = "King"
keyword = keyword.lower()

dict_book = {"matches": []}

for book in books:
    
    if keyword in book['title'].lower():
        dict_book["matches"].append(book)

print(dict_book["matches"])

""" 
    so far the aim is to be able to take a user input and print out results based on the input

    TODO:
        - Create a functional searchbar
"""