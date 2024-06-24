from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, DestroyAPIView
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as rest_filters
from .serializers import *
from Blog.models import Post
from Blog.pagination import CustomPagination
from Blog.permissions import IsOwner


class PostListCreateView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter, rest_filters.DjangoFilterBackend]
    filterset_fields = ['categories', 'tags']
    search_fields = ['title', 'content']
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile)


class PostRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile)

class CategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    pagination_class = CustomPagination
    permission_classes = []


class TagListApiView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = CustomPagination
    permission_classes = []


class CommentListCreateView(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile)


class CommentDestroyView(DestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile)