import unittest
from app.models import User,Blog
class UserTest(unittest.TestCase):
   def setUp(self):
       self.new_user = User(username = 'Kennedy',email='kennedykaruri99@gmail.com',bio='default bio',password='8410')
   def test_password_setter(self):
       self.assertTrue(self.new_user.pass_secure is not None)
   def test_no_password_access(self):
       with self.assertTrue(AttributeError):
           self.new_user.pass_secure
   def test_password_verification(self):
       self.assertTrue(self.new_user.verify_password('sharon'))