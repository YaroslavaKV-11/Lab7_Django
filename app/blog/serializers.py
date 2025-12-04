# blog/serializers.py
from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'text',
            'author',
            'publication_date',
            'article',   # id статті
            'user',
        ]
        read_only_fields = ['id', 'publication_date', 'user']


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    tag = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    user = serializers.StringRelatedField(read_only=True)

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'author',
            'user',
            'text',
            'image',
            'publication_date',
            'is_published',
            'category',
            'tag',
            'comments',
        ]
        read_only_fields = ['id', 'user', 'comments']
