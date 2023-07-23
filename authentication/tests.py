from django.test import TestCase
from authentication.models import User

# Create your tests here.
class UserSampleTestCase(TestCase):
    
    def setUp(self) -> None:
        User.objects.create(username="test1", password="test1", email="test1@gmail.com")
        User.objects.create(username="test2", password="test2", email="test2@gmail.com")
        User.objects.create(username="test3", password="test3", email="test3@gmail.com")
    
    # test_prefix for django to recognize that this method is a testcase
    def test_case_1(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.username, 'test1')
    
    # test_prefix for django to recognize that this method is a testcase
    def test_case_2(self):
        user = User.objects.get(id=2)
        # self.assertEqual(user.username, 'test21') # wrong test case
        self.assertEqual(user.username, 'test2')
    
    # test_prefix for django to recognize that this method is a testcase
    def test_case_3(self):
        user = User.objects.get(id=3)        
        self.assertEqual(user.username, 'test3')
        
    # test_prefix for django to recognize that this method is a testcase
    # wrong name
    def happy_case_4(self):
        user = User.objects.get(id=3)        
        self.assertEqual(user.username, 'test3')