
from django.test import TestCase
from apps.api.models import Books, Author, Category
from django.core.exceptions import ValidationError
from django.test import Client
 
class BooksTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.author = Author.objects.create(first_name='John', last_name='Doe')
        self.category = Category.objects.create(name='Floop')
        self.book = Books.objects.create(title='Dragonborne', published_date="1995-01-01", author=self.author, category=self.category, price=10, stock=5)


    # Creates an instance of Books
    def test_book_creation(self):
        self.assertEqual(self.book.title, 'Dragonborne')

    # Creates an instance of Author
    def test_author_creation(self):
        self.assertEqual(self.author.first_name, 'John')
        self.assertEqual(self.author.last_name, 'Doe')

    # Creates an instance of Category
    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Floop')

    # Creates an instance of Books with positive and negative stock
    def test_in_stock(self):
        self.book.stock = 5
        self.assertTrue(self.book.stock > 0)
        self.book.stock = 0
        self.assertFalse(self.book.stock > 0)
        self.book.stock = -1
        with self.assertRaises(ValidationError):
            self.book.clean()
    # Creates an instance of Books with positive and negative price
    def test_price(self):
        self.book.price = 5
        self.assertTrue(self.book.price > 0)
        self.book.price = 0
        self.assertFalse(self.book.price > 0)
        self.book.price = -1
        with self.assertRaises(ValidationError):
            self.book.clean()

    # Tests if the API can be accessed by the client
    def test_book_access(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        


    
        
    
        
    
    