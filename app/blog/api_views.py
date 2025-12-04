from rest_framework import generics
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer


class ArticleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.filter(is_published=True).order_by(
        "-publication_date"
    )
    serializer_class = ArticleSerializer


class ArticleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all().order_by("-publication_date")
    serializer_class = ArticleSerializer


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all().order_by("-publication_date")
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all().order_by("-publication_date")
    serializer_class = CommentSerializer
