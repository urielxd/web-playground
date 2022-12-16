from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCascade(TestCase):
    def setUp(self):
        User.objects.creat_user('test', 'test@test.com', 'test1234')

    def subTest_profile_exist(self):
        exists = Profile.objects.filter(user_username= 'test').exists()
        self.assertEqual(exists, True)