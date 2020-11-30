from django.urls import path

from .api_views import PostViewSet

urlpatterns = [
    path('posts/', PostViewSet.as_view({'get': 'get_all_posts'}), name='get_all_posts'),
    path('post/<int:pk>/', PostViewSet.as_view({'get': 'get_certain_post'}), name='get_certain_post'),
]
