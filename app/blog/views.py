from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Article, Category, Comment
from .forms import GuestCommentForm, AuthCommentForm

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

def _is_moderator(user):
    return user.is_authenticated and user.groups.filter(name='moderator').exists()

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk, is_published=True)
    return render(request, 'blog/article_detail.html',
                  {'article': article, 'is_moderator': _is_moderator(request.user)})

def category_list(request):
    categories = Category.objects.order_by('title')
    return render(request, 'blog/category_list.html', {'categories': categories})

def comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk, is_published=True)
    Form = AuthCommentForm if request.user.is_authenticated else GuestCommentForm

    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.article = article
            if request.user.is_authenticated:
                c.user = request.user
                if not c.author:
                    c.author = request.user.get_full_name() or request.user.get_username()
            c.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = Form()

    return render(request, 'blog/comment_form.html', {'form': form, 'article': article})

def comment_edit(request, pk, cid):
    c = get_object_or_404(Comment, pk=cid, article_id=pk)
    if not (request.user.is_authenticated and (c.user_id == request.user.id or _is_moderator(request.user))):
        return HttpResponseForbidden("Вам не можна редагувати цей коментар")

    if request.method == 'POST':
        form = AuthCommentForm(request.POST, instance=c)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=pk)
    else:
        form = AuthCommentForm(instance=c)
    return render(request, 'blog/comment_form.html', {'form': form, 'article': c.article, 'edit_mode': True})

def comment_delete(request, pk, cid):
    c = get_object_or_404(Comment, pk=cid, article_id=pk)
    if not (request.user.is_authenticated and (c.user_id == request.user.id or _is_moderator(request.user))):
        return HttpResponseForbidden("Вам не можна видаляти цей коментар")

    if request.method == 'POST':
        c.delete()
        return redirect('article_detail', pk=pk)
    return render(request, 'blog/comment_confirm_delete.html', {'comment': c})
