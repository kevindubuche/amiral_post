"""amiral_post URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from blog.views import home, post_details, posts_of_a_category, about, contact, sendmail
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', home, name='home'),
    path('sendmail/', sendmail, name='sendmail'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('article/<slug:slug>/', post_details, name='post_details'),
    path('category/<id>/', posts_of_a_category, name='category'),
    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),

    url(r'^public/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
