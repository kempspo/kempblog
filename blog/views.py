from django.views.generic import ListView, DetailView
from blog.models import Post, Note
from taggit.models import Tag
from itertools import chain

class List(ListView):
    model = Post
    def get_context_data(self, *args, **kwargs):
        context = super(List, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(status=1).order_by('-created_on')
        context['notes'] = Note.objects.filter(status=1).order_by('-created_on')
        return context
    template_name = 'index.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostList(DetailView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post_list.html'

class TagList(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        tags = Tag.objects.filter(slug=slug).values_list('name', flat=True)
        queryset = Post.objects.filter(tag__name__in=tags)

        return queryset

class NoteDetail(DetailView):
    model = Note
    template_name = 'note_detail.html'