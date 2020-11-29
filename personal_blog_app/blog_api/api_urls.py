from django.urls import path

from .api_views import PostViewSet

urlpatterns = [
    path('posts/', PostViewSet.as_view({'get': 'get_posts'}), name='posts')
]
