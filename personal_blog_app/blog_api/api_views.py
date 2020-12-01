from rest_framework import viewsets
from rest_framework.response import Response


from .api_serializers import PostsSerializer, PostSerializer
from ..models import Post


class PostsViewSet(viewsets.ViewSet):
    def get_posts(self, request):
        queryset = Post.objects.all()
        serializer = PostsSerializer(queryset, many=True)
        return Response(serializer.data)


class PostViewSet(viewsets.ViewSet):
    def get_post(self, request, pk):
        queryset = Post.objects.get(slug=pk)
        serializer = PostSerializer(queryset)
        return Response(serializer.data)
