from django.contrib import admin
from .models import Category, Tag, Article, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "icon")

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "publication_date", "is_published")
    list_filter = ("is_published", "category", "tag")
    search_fields = ("title", "author", "text")
    date_hierarchy = "publication_date"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "article", "publication_date")
    date_hierarchy = "publication_date"
