from django.shortcuts import render, get_object_or_404
from .models import Article, Category

def home(request):
    latest = (Article.objects
              .filter(is_published=True)
              .order_by('-publication_date')[:3])
    return render(request, 'blog/home.html', {'latest': latest})

def article_list(request):
    items = (Article.objects
             .filter(is_published=True)
             .order_by('-publication_date'))
    return render(request, 'blog/article_list.html', {'items': items})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk, is_published=True)
    return render(request, 'blog/article_detail.html', {'article': article})

def category_list(request):
    categories = Category.objects.order_by('title')
    return render(request, 'blog/category_list.html', {'categories': categories})
