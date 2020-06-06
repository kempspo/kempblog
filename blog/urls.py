from blog.views import PostDetail, PostList, TagList
from django.urls import path

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('blog/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('tag/<slug:slug>/', TagList.as_view(), name='tagged'),
]