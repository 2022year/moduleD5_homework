from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.core.paginator import Paginator
from .models import *
from .filters import PostFilter
from .forms import NewsForm
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


class PostsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')
    paginate_by = 10


class PostList(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostsSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        qs = self.get_filter().qs
        return qs


class PostsAdd(PermissionRequiredMixin, CreateView):
    permission_required = ('newspaper.add_post', )
    template_name = 'add.html'
    form_class = NewsForm
    success_url = '/news/'

# -----
class PostEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('newspaper.change_post', )
    template_name = 'edit.html'
    form_class = NewsForm
    success_url = '/news/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('newspaper.delete_post', )
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


def home(request):
    return render(request, 'home.html')
