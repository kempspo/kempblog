from django.contrib import admin
from .models import Post
from markdownx.admin import MarkdownxModelAdmin

@admin.register(Post)
class PostAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'slug', 'status','created_on','updated_on')
    list_filter = ('status','created_on','tag') 
    search_fields = ['title', 'content', 'tag']
    prepopulated_fields = {'slug': ('title',)}
  
# admin.site.register(Post, PostAdmin)