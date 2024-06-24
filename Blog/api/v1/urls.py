from django.urls import path
from .views import *
app_name = 'blog'

urlpatterns = [
    # Post #
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>', PostRetrieveUpdateDestroyView.as_view(), name='post-get-update-delete'),
    # Category #
    path('categories/', CategoryListApiView.as_view()),
    # Tag #
    path('tags/', TagListApiView.as_view()),
    # Comment #
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>', CommentDestroyView.as_view(), name='comment-destroy'),
]