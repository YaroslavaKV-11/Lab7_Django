from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.article_list, name='article_list'),
    path('articles/<int:pk>/', views.article_detail, name='article_detail'),
    path('categories/', views.category_list, name='category_list'),

    path('articles/<int:pk>/comment/new/', views.comment_create, name='comment_create'),
    path('articles/<int:pk>/comment/<int:cid>/edit/', views.comment_edit, name='comment_edit'),
    path('articles/<int:pk>/comment/<int:cid>/delete/', views.comment_delete, name='comment_delete'),
    path('api/', include('blog.api_urls')),
]
