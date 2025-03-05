from django.test import TestCase
from apps.cart.models import Cart
from apps.api.models import Books, Author, Category
from apps.accounts.models import CustomUser
from django.core.exceptions import ValidationError
from django.urls import reverse

# Create your tests here.


class CartsTestCase(TestCase):

    def setUp(self):
        # Create a user
        self.user = CustomUser.objects.create(username='Timothy', first_name='Timmy', last_name='Egbert', email='tim@tim.com')
        self.user.set_password('Password123?!')
        self.user.save()
        # Create an author    
        self.author = Author.objects.create(first_name='Jeff', last_name='Bezos')
        self.category = Category.objects.create(name='Fantasy')
        # Create a book
        self.book = Books.objects.create(title='Dragonborne', published_date="1995-01-01", author=self.author, category=self.category, price=10, stock=5)
        # Create a cart
        self.cart = Cart.objects.create(user_id=self.user, book=self.book)
        self.cart.save()

    def test_cart_creation(self):
        # Tests if the cart is created and user is assigned to the cart
        self.assertEqual(self.cart.user_id, self.user)
        # Tests if the cart is created and book is assigned to the cart
        self.assertEqual(self.cart.book, self.book)
        # Tests if the cart can access the book title
        self.assertEqual(self.cart.book.title, 'Dragonborne')
        # Tests if the cart can access the user username
        self.assertEqual(self.cart.user_id.username, 'Timothy')

    def test_cart_connection_to_cart(self):
        # Tests if the cart can be viewed without being logged in
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 302)

        #Tests if the cart can be viewed when logged ins
        self.client.login(username='Timothy', password='Password123?!')
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Basket')
    