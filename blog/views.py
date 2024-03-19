from django.shortcuts import render
from django.http import HttpRequest, Http404
from blog.data import posts

# Create your views here.

def blog(request):
    context1 = {
        'title': 'Blog Title',
        'text': 'Blog Text By Context1',
        'posts': posts,
    }
    
    return render(
        request, 
        'blog/index.html',
        context1,
    )
    
    
def post(request: HttpRequest, post_id: int):
    found_post = None
    
    for post in posts:
        if post["id"] == post_id:
            found_post = post
            
    if found_post is None:
        raise Http404('Page Not Found')
            
    context_post = {
        'title': found_post["title"],
        'text': 'Post Text By Context_Post',
        'post': found_post,
    }
    
    return render(
        request, 
        'blog/post.html',
        context_post,
    )


def example(request):
    context2 = {
        'title': 'Example Title',
        'text': 'Example Text By Context2',
    }
    
    return render(
        request, 
        'blog/example.html',
        context2,
    )