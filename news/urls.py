from django.urls import path
from .views import (
    NewPostView,
    NewDetailView,
    NewCreateView,
    NewUpdateView,
    NewDeleteView,
)

urlpatterns = [
    path('', NewPostView.as_view(), name = 'new_post'),
    path('post/<int:pk>/', NewDetailView.as_view(), name = 'new_detail'),
    path('post/create/', NewCreateView.as_view(), name = 'newp_create'),
    path('post/<int:pk>/update/', NewUpdateView.as_view(), name = 'newp_update'),
    path('post/<int:pk>/delete/', NewDeleteView.as_view(), name = 'newp_delete'),
]