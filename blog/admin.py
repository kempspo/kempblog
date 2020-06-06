from django.contrib import admin
from .models import Post, Note
from markdownx.admin import MarkdownxModelAdmin

@admin.register(Post)
class PostAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'slug', 'status','created_on','updated_on')
    list_filter = ('status','created_on','tag') 
    search_fields = ['title', 'content', 'tag']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Note)
class NoteAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'slug', 'status','created_on','updated_on')
    list_filter = ('status','created_on') 
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
