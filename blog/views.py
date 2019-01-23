from django.views import generic

from .models import Post
from main_app.models import Category


class PostListView(generic.ListView):
    model = Post
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
