from django.urls import path
from .views import (
    BlogPostView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    GeneralPostView,
)

urlpatterns = [
    path('home/post/<int:pk>/delete/', BlogDeleteView.as_view(), name = 'post_delete'),
    path('home/post/<int:pk>/edit/', BlogUpdateView.as_view(), name = 'post_edit'),
    path('home/post/new/', BlogCreateView.as_view(), name = 'post_new'),
    path('home/', BlogPostView.as_view(), name='home'),
    path('', GeneralPostView.as_view(), name = 'general'),
    path('home/post/<int:pk>/', BlogDetailView.as_view(), name = 'blog_detail'),
]