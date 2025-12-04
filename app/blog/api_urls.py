from django.urls import path
from . import api_views

urlpatterns = [
    path('articles/', api_views.ArticleListCreateAPIView.as_view(),
         name='api-article-list'),
    path('articles/<int:pk>/',
         api_views.ArticleRetrieveUpdateDestroyAPIView.as_view(),
         name='api-article-detail'),

    path('comments/', api_views.CommentListCreateAPIView.as_view(),
         name='api-comment-list'),
    path('comments/<int:pk>/',
         api_views.CommentRetrieveUpdateDestroyAPIView.as_view(),
         name='api-comment-detail'),
]
