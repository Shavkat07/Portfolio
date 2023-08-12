from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import *

app_name = 'blogs'

urlpatterns = [
    path('', BlogsListView.as_view(), name='blogs'),
    path('send_message/', CreateMessageView.as_view(), name='send_message'),
    path('page/<int:page>/', BlogsListView.as_view(), name='paginator'),
    path('blog/<int:blog_id>/', BlogsDetailView, name='blog_detail'),
    path('blog/comments/delete/<int:comment_id>', CommentDeleteView, name='comment_delete'),
    # path('like/<int:blog_id>', LikeBlog, name='like_blog'),
]
