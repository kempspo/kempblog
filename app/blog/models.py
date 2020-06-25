from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from markdownx.utils import markdownify
from markdownx.models import MarkdownxField
from taggit.managers import TaggableManager
from datetime import datetime

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    intro = models.TextField(max_length=1200)
    text = MarkdownxField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tag = TaggableManager()
    background_image = models.ImageField(upload_to=datetime.now().strftime('backgrounds/%Y/%m/%d'))

    # Create a property that returns the markdown instead
    @property
    def formatted_markdown(self):
        return markdownify(self.text)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            # 'created_on': self.created_on,
            'slug': self.slug,
        }
        return reverse('post_detail', kwargs=kwargs)

    class Meta():
        ordering = ['-created_on']


class Note(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = MarkdownxField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    # Create a property that returns the markdown instead
    @property
    def formatted_markdown(self):
        return markdownify(self.text)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            # 'created_on': self.created_on,
            'slug': self.slug,
        }
        return reverse('post_detail', kwargs=kwargs)

    class Meta():
        ordering = ['-created_on']
