from django.shortcuts import render
from .models import About


def index(request):
    feedbacks = About.objects.all()
    context = {
        'feedbacks': feedbacks
    }
    return render(request, 'readit/about.html', context)
