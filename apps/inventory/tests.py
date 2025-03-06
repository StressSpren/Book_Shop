from django.test import TestCase
from apps.accounts.models import CustomUser
from apps.api.models import Books, Author, Category
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.
 

class DisplayPageTestCase(TestCase):

    def setUp(self):

        # Create a user
        self.user = CustomUser.objects.create(username='Timothy', first_name='Timmy', last_name='Egbert')
        self.user.set_password('Password123?!')
        self.user.save()

        # Create an author
        self.author = Author.objects.create(first_name='Dave', last_name='Davidson')
        self.category = Category.objects.create(name='Fantasy')

        # Create a book
        img = SimpleUploadedFile(name='lotr.jpg', content=b'book_pics', content_type='image/jpg')
        self.book = Books.objects.create(title='Dragonborne', published_date="1995-01-01", author=self.author, category=self.category, cover_image = img, price=10, stock=5)
        self.book.save()
     

    def test_home_page(self):

        # Test expecting a error code 302 as no response should be given without being logged in
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)
        
        # Test expecting a error code 200 as a response should be given when logged in
        self.client.login(username='Timothy', password='Password123?!')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

        # As home page contains a Basket only a logged in user should see
        self.assertContains(response, 'Basket')

        # Tests if the book is created and displayed on the home page
        self.assertContains(response, 'Dragonborne')

    def test_genre_page(self):

        # Test expecting a error code 302 as no response should be given without being logged in
        response = self.client.get(reverse('genres'))
        self.assertEqual(response.status_code, 302)

        # Test expecting a error code 200 as a response should be given when logged in
        self.client.login(username='Timothy', password='Password123?!')
        response = self.client.get(reverse('genres'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Genres')

        # Tests if the Fantasy Row is created when a book is created in the Fantasy category
        self.assertContains(response, 'Fantasy')

    def test_search_page(self):

        # Test expecting a error code 302 as no response should be given without being logged in
        response = self.client.get(reverse('search_books'))
        self.assertEqual(response.status_code, 302)

        # Test expecting a error code 200 as a response should be given when logged in
        self.client.login(username='Timothy', password='Password123?!')
        response = self.client.get(reverse('search_books'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Search')

    