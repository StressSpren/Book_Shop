from django.test import TestCase
from apps.accounts.models import CustomUser
from django.core.exceptions import ValidationError
 
class UserTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='Timothy', first_name='Timmy', last_name='Egbert', email="Tim@Tim.com")
        self.user.set_password('Password123?!')
        self.user.save()
        
    # Creates an isntance of CustomUser 
    def test_user_creation(self):
        self.assertEqual(self.user.username, 'Timothy')
        self.assertEqual(self.user.first_name, 'Timmy')
        self.assertEqual(self.user.last_name, 'Egbert')
        self.assertEqual(self.user.email, 'Tim@Tim.com')

    # Creates an instance of CustomUser and checks if password is hashed
    def test_password_hash(self):
        # Check if password is hashed
        self.assertEqual(self.user.password.startswith('pbkdf2_sha256'), True)
        self.assertEqual(self.user.password.startswith('Password123?!'), False)

 