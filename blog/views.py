from django.shortcuts import render
from django.utils import timezone
# Поскольку views.py и models.py находятся в одной директории, мы можем использовать точку . и имя файла (без расширения .py)
from .models import Post

def post_list(request):
    #posts = Post.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
