from django.views.generic import ListView, DetailView
from blog.models import Post
from taggit.models import Tag

class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

class TagList(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        tags = Tag.objects.filter(slug=slug).values_list('name', flat=True)
        queryset = Post.objects.filter(tag__name__in=tags)

        return queryset