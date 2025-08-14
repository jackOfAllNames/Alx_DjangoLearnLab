from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserRegistrationForm, UserProfileUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User


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


class ProfileUpdateView(UpdateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    template_name = 'blog/profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user 


def ProfileView(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserProfileUpdateForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'blog/profile.html', context)