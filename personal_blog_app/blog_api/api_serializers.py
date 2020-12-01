from rest_framework import serializers
from ..models import Post


class PostsSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    status = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ['title',
                  'publication_date',
                  'author',
                  'content']
