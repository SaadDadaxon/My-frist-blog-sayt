from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Article, Category, Tag
from .forms import CommentForm


def index(request):
    articles = Article.objects.order_by('-id')
    page_number = request.GET.get('page', 1)
    paginator = Paginator(articles, 1)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)
    context = {
        'object_list': page_obj
    }
    return render(request, 'readit/index.html', context)


def article_list(request):
    articles = Article.objects.order_by('-id')
    cate = request.GET.get('cate')
    tag = request.GET.get('tag')
    search = request.GET.get('search')
    if cate:
        articles = articles.filter(category__title__exact=cate)
    if tag:
        articles = articles.filter(tags__title__exact=tag)
    if search:
        articles = articles.filter(title__icontains=search)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(articles, 1)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)
    context = {
        'object_list': page_obj
    }
    return render(request, 'readit/blog.html', context)


def article_detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    categories = Category.objects.all()
    tags_1 = Tag.objects.all()
    lists = Article.objects.order_by('-id')[:3]
    form = CommentForm()
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect(reverse('blog:detail', kwargs={'pk': article.id}))
        form = CommentForm(data=request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author_id = request.user.profile.id
            obj.article_id = article.id
            obj.save()
            return redirect('.')
    context = {
        'object': article,
        'categories': categories,
        'lists': lists,
        'tags_1': tags_1,
        'form': form,
    }
    return render(request, 'readit/blog-single.html', context)



