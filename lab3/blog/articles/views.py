from django.shortcuts import render
from .models import Article

def archive(request):
    posts = Article.objects.all()
    return render(request, 'archive.html', {"posts": Article.objects.all()})

# Create your views here.
