from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category, Pub

class PostAdmin(SummernoteModelAdmin):
    exclude = ('slug', )
    list_display = ('title', 'category', 'date_added')
    list_display_links = ('title',)
    search_fields = ('title', )
    list_per_page = 15
    summernote_fields = ('content', )

# class PubAdmin(Pub):
#     list_display = ('title','link')
#     list_display_links = ('tile','link',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Pub)

admin.site.site_header = 'Amiral Post'