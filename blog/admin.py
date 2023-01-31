from django.contrib import admin
from .models import Article, Tag, Category, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_date']
    list_filter = ['category', 'tags']
    date_hierarchy = 'created_date'
    filter_horizontal = ('tags',)
    search_fields = ['title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Category)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'article', 'created_date']
    date_hierarchy = 'created_date'
    search_fields = ['author__username', 'article__title', 'author__first_name', 'author__last_name']
    autocomplete_fields = ['author', 'article']


