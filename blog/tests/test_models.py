from django.test import TestCase

from blog.models import Blog, Comment, Author

class BlogModelTest(TestCase):
    blog = None
    @classmethod
    def setUpTestData(cls):
        cls.blog = Blog.objects.create(title='blog', post='lorem ipsum')

        # test_user1 = User.objects.create_user(username='testuser1', password='12345')
        # test_user1.save()


    def test_max_length_title(self):
        max_length = self.blog._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_max_length_post(self):

        max_length = self.blog._meta.get_field('post').max_length
        self.assertEqual(max_length, 1000)

    def test_lable_title(self):

        lable = self.blog._meta.get_field('title').verbose_name
        self.assertEqual(lable, 'title')

    def test_label_post(self):

        lable = self.blog._meta.get_field('post').verbose_name
        self.assertEqual(lable, 'post')

    def test_str(self):

        str = self.blog.__str__()
        self.assertEqual(str, 'blog')

    def test_url(self):
        url = self.blog.get_absolute_url()
        self.assertEqual(url, '/blog/blog/1')

class AuthorModelTest(TestCase):
    author = None
    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(first_name='fred', last_name='smith', bio='lorem ipsum')


    def test_max_first_name(self):
        max_length = self.author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_max_last_name(self):
        max_length = self.author._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 100)

    def test_max_bio(self):
        max_length = self.author._meta.get_field('bio').max_length
        self.assertEqual(max_length, 1000)

    def test_lable_first_name(self):
        lable = self.author._meta.get_field('first_name').verbose_name
        self.assertEqual(lable, 'first name')

    def test_lable_last_name(self):
        lable = self.author._meta.get_field('last_name').verbose_name
        self.assertEqual(lable, 'last name')

    def test_label_bio(self):
        lable = self.author._meta.get_field('bio').verbose_name
        self.assertEqual(lable, 'bio')

    def test_str(self):
        str = self.author.__str__()
        self.assertEqual(str, self.author.first_name + ' ' + self.author.last_name)

    def test_url(self):
        url = self.author.get_absolute_url()
        self.assertEqual(url, '/blog/author/1')

