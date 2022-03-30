from django.shortcuts import render
from django.views import generic
from .models import Post

class Post_List(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-time_created')
    template_name = 'blog/index.html'


