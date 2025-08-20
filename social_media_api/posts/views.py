from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer

class PostAPIView(viewsets.ModelViewSet):
    """
    A view to handle API requests related to posts.
    This view will handle creating, retrieving, updating, and deleting posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

