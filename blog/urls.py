from blog.views import PostDetail, List, TagList, NoteDetail, PostList
from django.urls import path

urlpatterns = [
    path('', List.as_view(), name='home'),
    path('blog/', PostList.as_view(), name='post_list'),
    path('blog/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('tag/<slug:slug>/', TagList.as_view(), name='tagged'),
    path('note/<slug:slug>/', NoteDetail.as_view(), name='note_detail'),
]