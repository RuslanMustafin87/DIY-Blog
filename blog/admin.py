from django.contrib import admin
from .models import Blog, Author, Comment
# Register your models here.

# admin.site.register(Blog)

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'post', 'data_post', 'author')
    inlines = [CommentInline]

class BlogInline(admin.StackedInline):
    model = Blog
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'bio')
    fields = [('first_name', 'last_name'), 'user', 'bio']
    inlines = [BlogInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'blog', 'data_post', 'user')