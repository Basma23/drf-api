from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

# Create your tests here.

class FruitsTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create(username='user', password='password')
        test_user.save()
        test_post = Post.objects.create(author=test_user, title='Django REST Framework And Docker', description='Docker is really just Linux containers which are a type of virtualization.')
        test_post.save()


    def test_fruits_content(self):
        post = Post.objects.get(id=1)
        actual_author = str(post.author)
        actual_title = str(post.title)
        actual_description = str(post.description)
        self.assertEqual(actual_author, 'user')
        self.assertEqual(actual_title, 'Django REST Framework And Docker')
        self.assertEqual(actual_description, 'Docker is really just Linux containers which are a type of virtualization.')
