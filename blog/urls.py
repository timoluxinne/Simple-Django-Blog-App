from django.urls import path
from .views import PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('post-detail/<str:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post-update/<str:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post-delete/<str:pk>/', PostDeleteView.as_view(), name='post-delete'),
]
