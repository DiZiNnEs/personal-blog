from django.urls import path

from .api_views import PostViewSet, PostsViewSet

urlpatterns = [
    path('posts/', PostsViewSet.as_view({'get': 'get_posts'}), name='get_all_posts'),
    path('post/<int:pk>/', PostViewSet.as_view({'get': 'get_post'}), name='get_certain_post'),
]
