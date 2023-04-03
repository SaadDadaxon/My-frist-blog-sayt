from rest_framework import generics, permissions
from .permission import IsOwnerOrReadOnly

from .serializers import CategorySerializer, TagSerializer, ArticleGETSerializer, ArticlePOSTSerializer, CommentGETSerializer
from ..models import Category, Tag, Article, Comment


class CategoryListCreateAPI(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListCreateAPI(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ArticleListCreate(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleGETSerializer
        return ArticlePOSTSerializer


class ArticleRUDAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleGETSerializer
        return ArticlePOSTSerializer


class CommentListCreateAPI(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentGETSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        article_id = self.kwargs.get('article_id')
        if qs:
            qs = qs.filter(article_id=article_id)
            return qs
        return []

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['article_id'] = self.kwargs.get('article_id')
        return ctx


