from django.urls import path
from .views import PostDetailView, PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post-detail/<str:pk>/', PostDetailView.as_view(), name='post-detail'),
]
