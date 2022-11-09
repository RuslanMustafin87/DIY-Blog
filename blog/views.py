from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog, Author, Comment
# from .forms import NewCommentForm

# Create your views here.
def index(request):

    return render(request, 'index.html')


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5

class BlogDetailView(generic.DetailView):
    model = Blog

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author

# @login_required
# def new_comment(request, pk):

#     if request.method == 'POST':

#         form = NewCommentForm(request.POST)
#         if form.is_valid():
#             comment = Comment()
#             comment.text = form.cleaned_data['text']
#             comment.user = request.user
#             comment.blog = get_object_or_404(Blog, pk=pk)
#             comment.save()

#             return HttpResponseRedirect(reverse('blog-detail', kwargs={'pk': pk}))
#     else:
#         form = NewCommentForm()

#     return render(request, 'blog/create_new_comment.html', {'form': form})

class CommentCreate(LoginRequiredMixin, generic.CreateView):
    model = Comment
    fields = ['text']

    def get_success_url(self):
        return reverse_lazy('blog-detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):

        form.instance.user = self.request.user
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])

        return super(CommentCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):

        context = super(CommentCreate, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])

        return context

