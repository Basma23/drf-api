from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

# Create your tests here.

class BlogTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create(username='user', password='password')
        test_user.save()
        test_post = Post.objects.create(author=test_user, title='Django REST Framework And Docker', body='Docker is really just Linux containers which are a type of virtualization.')
        test_post.save()


    def test_blog_content(self):
        post = Post.objects.get(id=1)
        actual_author = str(post.author)
        actual_title = str(post.title)
        actual_body = str(post.body)
        self.assertEqual(actual_author, 'user')
        self.assertEqual(actual_title, 'Django REST Framework And Docker')
        self.assertEqual(actual_body, 'Docker is really just Linux containers which are a type of virtualization.')
