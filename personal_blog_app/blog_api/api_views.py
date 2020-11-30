from rest_framework import viewsets
from rest_framework.response import Response


from .api_serializers import PostSerializer
from ..models import Post


class PostViewSet(viewsets.ViewSet):
    def get_all_posts(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_certain_post(self, request, pk):
        queryset = Post.objects.get(slug=pk)
        serializer = PostSerializer(queryset)
        return Response(serializer.data)

