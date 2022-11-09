from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^blogs/$', views.BlogListView.as_view(), name='blog-list'),
    re_path(r'^blog/(?P<pk>\d+)$', views.BlogDetailView.as_view(), name='blog-detail'),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='author-list'),
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    re_path(r'^blog/(?P<pk>\d+)/create/$', views.CommentCreate.as_view(), name='comment-create'),
    # re_path(r'^blog/(?P<pk>\d+)/create/$', views.new_comment, name='comment-create'),
]