from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserRegistrationForm
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'blog/index.html'


class SignUpView(CreateView):
    form_class = CustomUserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'blog/signup.html'


class LogInView(LoginView):
    template_name = 'blog/login.html'
    next_page = reverse_lazy('home')


class LogOutView(LogoutView):
    next_page = reverse_lazy('home')
    template_name = 'blog/logged_out.html'
