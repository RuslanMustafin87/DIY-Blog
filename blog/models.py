from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, help_text='Post title')
    post = models.TextField(max_length=1000, help_text='Enter a post')
    data_post = models.DateField(default=date.today)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    class Meta:
        ordering = ['-data_post']

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=1000, blank=True, null=True, help_text='Enter bio of the author')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


class Comment(models.Model):
    text = models.TextField(max_length=1000, help_text='text of the comment')
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)
    data_post = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text if len(self.text) < 75 else self.text[:75] + '...'

    class Meta:
        ordering = ['-data_post']

