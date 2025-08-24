from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

class PostAPIView(viewsets.ModelViewSet):
    """
    A view to handle API requests related to posts.
    This view will handle creating, retrieving, updating, and deleting posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentAPIView(viewsets.ModelViewSet):
    """
    A view to handle API requests related to comments.
    This view will handle creating, retrieving, updating, and deleting comments.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        following_users = self.request.user.following.all()

        users_to_include = list(following_users) + [self.request.user]

        return Post.objects.filter(author__in=following_users).order_by('-created_at')


class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({"detail": "You already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

        # Create notification
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked",
            target=post,
            content_type=ContentType.objects.get_for_model(Post)
        )

        return Response({"detail": "Post liked"}, status=status.HTTP_200_OK)


class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()
        if like:
            like.delete()
            return Response({"detail": "Post unliked"}, status=status.HTTP_200_OK)
        return Response({"detail": "You have not liked this post"}, status=status.HTTP_400_BAD_REQUEST)
