from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ('title', 'content')
    template_name = 'blog/post_edit.html'
    context_object_name = 'post'
    login_url = 'login'

    # In this case, as with the form_valid function in the create view below,
    # this is essentially overriding a native UpdateView function called dispatch
    # to do something custom, then calling the overriden native function
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    context_object_name = 'post'
    fields = ('title', 'content')

    # Since this is using LoginRequiredMixin, this lets django know where
    # to redirect a user who tries to access this view without being logged in,
    # in this case the login page
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
