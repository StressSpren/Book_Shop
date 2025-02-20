import requests


# url = f"http://127.0.0.1:8000/api/books"
# response = requests.get(url)
# response.raise_for_status()
# data = response.json()
# books = data.get('results', [])
# print(books)
# keyword = "King"
# keyword = keyword.lower()

# dict_book = {"matches": []}

# for book in books:
    
#     if keyword in book['title'].lower():
#         dict_book["matches"].append(book)

# print(dict_book["matches"])



# """
#     Connecting to an API and extracting results
# """
# url = 'http://127.0.0.1:8000/api/books'
# response = requests.get(url) # makes a request to the api
# response.raise_for_status() # error checks to make sure its okay
# data = response.json() # converts the repsonse into a json format


# books = data.get('results', []) # assigns books to the 'results' directory




# '''
#     Using Patch to change the values within the database
# '''
# url = 'http://127.0.0.1:8000/api/books/1'

# response = requests.get(url)
# response.raise_for_status()

# data = response.json()

# todo={"stock": 2}

# data = requests.patch(url, json=todo)



# import requests

# url = f"http://127.0.0.1:8000/api/books/1"

# response = requests.get(url)
# response.raise_for_status()
# data = response.json()

# print(data)