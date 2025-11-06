from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group
from .models import Article, Comment, Category
from .forms import GuestCommentForm, AuthCommentForm

def is_moderator(user):
    return user.is_authenticated and user.groups.filter(name='moderator').exists()

def comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk, is_published=True)
    Form = AuthCommentForm if request.user.is_authenticated else GuestCommentForm

    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            if request.user.is_authenticated:
                comment.user = request.user
                if not comment.author:
                    comment.author = request.user.get_full_name() or request.user.get_username()
            comment.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = Form()

    return render(request, 'blog/comment_form.html', {'form': form, 'article': article})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk, is_published=True)
    return render(request, 'blog/article_detail.html',
                  {'article': article, 'is_moderator': is_moderator(request.user)})

def comment_edit(request, pk, cid):
    comment = get_object_or_404(Comment, pk=cid, article_id=pk)
    if not (request.user.is_authenticated and (comment.user_id == request.user.id or is_moderator(request.user))):
        return HttpResponseForbidden("Вам не можна редагувати цей коментар")

    if request.method == 'POST':
        form = AuthCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=pk)
    else:
        form = AuthCommentForm(instance=comment)
    return render(request, 'blog/comment_form.html', {'form': form, 'article': comment.article, 'edit_mode': True})

def comment_delete(request, pk, cid):
    comment = get_object_or_404(Comment, pk=cid, article_id=pk)
    if not (request.user.is_authenticated and (comment.user_id == request.user.id or is_moderator(request.user))):
        return HttpResponseForbidden("Вам не можна видаляти цей коментар")

    if request.method == 'POST':
        comment.delete()
        return redirect('article_detail', pk=pk)
    return render(request, 'blog/comment_confirm_delete.html', {'comment': comment})
