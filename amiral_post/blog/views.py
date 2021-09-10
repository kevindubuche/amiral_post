from django.core import paginator
from django.shortcuts import render

from .models import Category, Post
from django.core.paginator import Paginator

def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    last_five_posts = Post.objects.order_by('-id')[:5]
    return render(request, 'blog/Home/home.html', {'posts': posts, 'categories': categories, 'last_five_posts':last_five_posts})

def post_details(request, slug):
    post = Post.objects.get(slug=slug)
    categories = Category.objects.all()
    return render(request, 'blog/PostDetails/post_details.html', {'post': post, 'categories': categories})

def posts_of_a_category(request, id):
    posts = Post.objects.order_by('-date_added').filter(category__id=id)
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    categories = Category.objects.all()
    return render(request, 'blog/Category/posts_of_a_category.html', {'posts': posts, 'categories': categories})

def about(request):
    categories = Category.objects.all()
    return render(request, 'blog/About/about.html', {'categories': categories})

def contact(request):
    categories = Category.objects.all()
    return render(request, 'blog/Contact/contact.html', {'categories': categories})