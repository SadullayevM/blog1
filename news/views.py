from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import NewPostModel
# Create your views here.
class NewPostView(ListView):
    model = NewPostModel
    template_name = 'new_post.html'

class NewDetailView(DetailView):
    model = NewPostModel
    template_name = 'new_detail.html'
    context_object_name = "post"

class NewCreateView(CreateView):
    model = NewPostModel
    template_name = 'newp_create.html'
    fields = ['title', 'author', 'text']

class NewUpdateView(UpdateView):
    model = NewPostModel
    template_name = 'newp_update.html'
    fields = ['title', 'text']

class NewDeleteView(DeleteView):
    model = NewPostModel
    template_name = 'newp_delete.html'
    success_url = reverse_lazy('new_post')
