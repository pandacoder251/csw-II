from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
    post_list = Post.published.all()  # only published posts
    paginator = Paginator(post_list, 3)  # 3 posts per page
    page_number = request.GET.get('page')

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)  # fallback to first page
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)  # fallback to last page

    # Pass both 'posts' and 'page_obj' so template can use either
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts, 'page_obj': posts}
    )

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=slug,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    return render(request, 'blog/post/detail.html', {'post': post})