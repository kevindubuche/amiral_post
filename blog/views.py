from django.core import paginator
from django.shortcuts import render
from .models import Category, Post, Pub, Team
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def sendmail(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        message = '''
        Nouveau message: {}

        De: {}
        '''.format(data['message'],data['email'])
        try:
            send_mail(data['subject'],
            message,
            '',
            ['Amiralpostssubmit@gmail.com'],
            fail_silently=False
            )
            messages.success(request, 'Message envoyé !')
        except :
            messages.error(request, "Message non envoyé. Essayez plus tard.")

        return redirect('home')

def home(request): 
    categories = Category.objects.all()
    # HANDLE THE SEARCH ENGINE
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        posts = Post.objects.filter(keywords__icontains = keyword)
        paginator = Paginator(posts, 8)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        try:
            pub = Pub.objects.all()[0]
        except :
            pub = None
        return render(request, 'blog/Category/posts_of_a_category.html', {'posts': posts, 'categories': categories,'pub': pub})
    # HANDLE THE SEARCH ENGINE___END
    filter_fields = ("category")
    posts = Post.objects.all()
    try:
        last_post_of_category_national = Post.objects.filter(category__name__iexact = 'national')[0]
    except :
        last_post_of_category_national = None
    try:
        last_post_of_category_international = Post.objects.filter(category__name__iexact = 'international')[0]
    except :
        last_post_of_category_international = None
    try:
       last_post_of_category_diplomatie = Post.objects.filter(category__name__iexact = 'diplomatie')[0]
    except :
        last_post_of_category_diplomatie = None
    try:
       last_post_of_category_economie = Post.objects.filter(category__name__iexact = 'Économie')[0]
    except :
        last_post_of_category_economie = None
    try:
       last_post_of_category_culture_et_sport = Post.objects.filter(category__name__iexact = 'culture et sport')[0]
    except :
        last_post_of_category_culture_et_sport = None
    try:
       random_5_posts_of_category_culture_et_sport = Post.objects.filter(category__name__iexact = 'culture et sport').order_by('?')[:5]
    except :
        random_5_posts_of_category_culture_et_sport = None
    try:
       random_3_posts_of_category_international = Post.objects.filter(category__name__iexact = 'international').order_by('?')[:3]
    except :
        random_3_posts_of_category_international = None
   
    try:
        last_five_posts = Post.objects.order_by('-id')[:5]
    except :
       last_five_posts = None
    context = {'posts': posts, 'categories': categories, 'last_five_posts':last_five_posts, 'last_post_of_category_national': last_post_of_category_national, 'last_post_of_category_international': last_post_of_category_international, 'last_post_of_category_diplomatie' : last_post_of_category_diplomatie, 'last_post_of_category_culture_et_sport': last_post_of_category_culture_et_sport, 'random_5_posts_of_category_culture_et_sport': random_5_posts_of_category_culture_et_sport, 'random_3_posts_of_category_international': random_3_posts_of_category_international, 'last_post_of_category_economie': last_post_of_category_economie}
    return render(request, 'blog/Home/home.html', context)

def post_details(request, slug):
    post = Post.objects.get(slug=slug)
    categories = Category.objects.all()
    try:
       random_3_posts = Post.objects.all().order_by('?')[:3]
    except :
        random_3_posts = None
    return render(request, 'blog/PostDetails/post_details.html', {'post': post, 'categories': categories, 'random_3_posts':random_3_posts})

def posts_of_a_category(request, id):
    posts = Post.objects.order_by('-date_added').filter(category__id=id)
    paginator = Paginator(posts, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    categories = Category.objects.all()
    try:
       pub = Pub.objects.all()[0]
    except :
        pub = None
    return render(request, 'blog/Category/posts_of_a_category.html', {'posts': posts, 'categories': categories, 'pub': pub })

def about(request):
    categories = Category.objects.all()
    teams = Team.objects.all()
    return render(request, 'blog/About/about.html', {'categories': categories, 'teams' : teams })

def contact(request):
    categories = Category.objects.all()
    return render(request, 'blog/Contact/contact.html', {'categories': categories})