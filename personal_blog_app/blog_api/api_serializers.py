from rest_framework import serializers
from ..models import Post


class PostsSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ['title',
                  'publication_date',
                  'author',
                  'slug', ]


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ['title',
                  'publication_date',
                  'author',
                  'content',
                  'status', ]
