from django.test import TestCase

# from blog.views import BlogListView
from blog.models import Blog, Author
from django.contrib.auth.models import User
from django.urls import reverse

class BlogListViewTest(TestCase):

    # @classmethod
    # def setUpTestData(cls):
    # @classmethod
    def setUp(self):
        test_user = User.objects.create_user(username='ruslan', password='123456')
        test_user.save()
        author = Author.objects.create(first_name='ruslan', last_name='mustafin', user=test_user, bio='lorem ipsunm')

        for i in range(15):
            Blog.objects.create(title='Blog', author=author, post='This is a test')

    def test_exist_by_url(self):
        resp = self.client.get('/blog/blogs/')
        self.assertEqual(resp.status_code, 200)

    def test_exist_by_url2(self):
        resp = self.client.get(reverse('blog-list'))
        self.assertEqual(resp.status_code, 200)

    def test_correct_template(self):
        resp = self.client.get(reverse('blog-list'))
        self.assertTemplateUsed(resp, 'blog/blog_list.html')

    def test_uses_pagination(self):
        resp = self.client.get(reverse('blog-list'))
        self.assertEqual(len(resp.context['blog_list']), 5)


