from django.urls import path
from .views import PostCreateView, PostDetailView, PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('post/post-detail/<str:pk>/', PostDetailView.as_view(), name='post-detail'),
]
