from django.shortcuts import render
from django.http import JsonResponse

def HomeView(request):
    return JsonResponse({"message": "Welcome to the Social Media API!"})
    
