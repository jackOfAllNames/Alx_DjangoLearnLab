from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserRegistrationForm
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'blog/index.html'


class SignUpView(CreateView):
    form_class = CustomUserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class LoginView(TemplateView):
    template_name = 'registration/login.html'
