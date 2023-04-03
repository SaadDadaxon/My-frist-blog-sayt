from django.urls import path
from .views import CategoryListCreateAPI, TagListCreateAPI, ArticleListCreate, ArticleRUDAPI, CommentListCreateAPI

urlpatterns = [
    path('category-list-create/', CategoryListCreateAPI.as_view()),
    path('tag-list-create/', TagListCreateAPI.as_view()),
    path('article-list-create/', ArticleListCreate.as_view()),
    path('article-rud/<int:pk>/', ArticleRUDAPI.as_view()),
    path('article/<int:article_id>/comment-list-create/', CommentListCreateAPI.as_view()),
]
