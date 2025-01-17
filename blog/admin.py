from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category, Pub, Team

class PostAdmin(SummernoteModelAdmin):
    exclude = ('slug', )
    list_display = ('title', 'category', 'date_added')
    list_display_links = ('title',)
    search_fields = ('title', )
    list_per_page = 15
    summernote_fields = ('content', )

class PubAdmin(admin.ModelAdmin):
    list_display = ('title','link')
    list_display_links = ('title','link',)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'title',)
    list_display_links = ('name', 'title',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Pub, PubAdmin)
admin.site.register(Team, TeamAdmin)

admin.site.site_header = 'Amiral Posts'