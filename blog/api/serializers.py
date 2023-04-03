from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import Article, Tag, Category, Comment
from profile.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class AuthorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'avatar', 'bio']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

    def validate(self, attrs):
        title = attrs.get('title')
        if title.islower():
            raise ValidationError({"title": "First letter of title must be uppercase"})
        return attrs


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']

    def validate(self, attrs):
        title = attrs.get('title')
        if title.islower():
            raise ValidationError({"title": "First letter of title must be uppercase"})
        return attrs


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'body', 'created_date']


class ArticleGETSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    author = AuthorSerializer(read_only=True)
    comment_list = CommentSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'category', 'image', 'description', 'comment_list', 'tags', 'created_date']


class ArticlePOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'category', 'image', 'description', 'tags', 'created_date']

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user.profile
        instance = super().create(validated_data)
        instance.author = author
        instance.save()
        return instance


class CommentGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'article', 'body', 'created_date']
        extra_kwargs = {
            'article': {'required': False}
        }

    def create(self, validated_data):
        request = self.context.get('request')
        article_id = self.context.get('article_id')
        author_id = request.user.profile.id
        body = validated_data.get('body')
        instance = Comment.objects.create(author_id=author_id, article_id=article_id, body=body)
        return instance

