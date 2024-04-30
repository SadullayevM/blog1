from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPostModel
# Create your views here.

class GeneralPostView(TemplateView):
    template_name = 'general.html'
class BlogPostView(ListView):
    model = BlogPostModel
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = BlogPostModel
    template_name = 'blog_detail.html'
    context_object_name = "post"

class BlogCreateView(CreateView):
    model = BlogPostModel
    template_name = 'post_new.html'
    fields = ['title', 'author', 'text']

class BlogUpdateView(UpdateView):
    model = BlogPostModel
    template_name = 'post_edit.html'
    fields = ['title', 'text']

class BlogDeleteView(DeleteView):
    model = BlogPostModel
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    context_object_name = 'post'