from django.shortcuts import render, HttpResponse
from django.views import generic
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


class PostList(generic.ListView):
    model = Post
    template_name = 'index.html'


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats': cats, 'category_posts':category_posts})


class DetailPostView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    fields = ['title', 'content']


class AddPostView(generic.CreateView):
    model = Post
    template_name = 'add_post.html'
    # fields = ['title', 'author', 'content']
    form_class = PostForm


class UpdatePostView(generic.UpdateView):
    model = Post
    template_name = 'update_post.html'
    # fields = ['title', 'content']
    form_class = EditForm


class DeletePostView(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddCategoryView(generic.CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
