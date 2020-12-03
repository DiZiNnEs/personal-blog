from rest_framework import viewsets
from rest_framework.response import Response

from .api_serializers import PostsSerializer, PostSerializer
from ..models import Post


class PostsViewSet(viewsets.ViewSet):
    def get_posts(self, request):
        try:
            return self.__get_posts()
        except Exception as ex:
            raise ex

    def __get_posts(self):
        queryset = Post.objects.all().order_by('-publication_date')
        serializer = PostsSerializer(queryset, many=True)
        return Response(serializer.data)


class PostViewSet(viewsets.ViewSet):
    def get_post(self, request, pk):
        try:
            return self.__get_post(pk)
        except Exception as ex:
            raise ex

    def __get_post(self, pk):
        queryset = Post.objects.get(slug=pk)
        serializer = PostSerializer(queryset)
        return Response(serializer.data)
