from django.urls import path
from .views import PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('posts/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post-detail/<str:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post-update/<str:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post-delete/<str:pk>/', PostDeleteView.as_view(), name='post-delete'),
]
