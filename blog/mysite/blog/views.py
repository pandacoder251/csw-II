from django.shortcuts import render, get_object_or_404
from .models import Post

# List all published posts
def post_list(request):
    posts = Post.objects.filter(status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/list.html', {'posts': posts})

# Show details of a single post
def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post})