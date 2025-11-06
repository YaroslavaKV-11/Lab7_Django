from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200)

    author = models.CharField(max_length=100, blank=True)

    user = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.SET_NULL, related_name='articles'
    )

    text = models.TextField()
    image = models.URLField(blank=True)
    publication_date = models.DateField()
    is_published = models.BooleanField(default=True)

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='articles'
    )

    tag = models.ManyToManyField(Tag, blank=True, related_name='articles')

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()

    author = models.CharField(max_length=100, blank=True)

    publication_date = models.DateField(auto_now_add=True)

    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comments'
    )

    user = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.SET_NULL, related_name='comments'
    )

    def __str__(self):
        who = self.author or (self.user.get_username() if self.user else "anon")
        return f"{who}: {self.text[:30]}"
