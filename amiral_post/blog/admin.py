from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category

class PostAdmin(SummernoteModelAdmin):
    exclude = ('slug', )
    list_display = ('title', 'category', 'date_added')
    list_display_links = ('title',)
    search_fields = ('title', )
    list_per_page = 15
    summernote_fields = ('content', )

admin.site.register(Post, PostAdmin)
admin.site.register(Category)

admin.site.site_header = 'Amiral Post'