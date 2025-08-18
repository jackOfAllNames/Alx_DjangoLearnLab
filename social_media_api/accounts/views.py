from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from django.contrib.auth import get_user_model

from .serializers import UserSerializer


User = get_user_model()


def HomeView(request):
    return JsonResponse({"message": "Welcome to the Social Media API!"})
    

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
