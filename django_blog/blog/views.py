from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DeleteView, DetailView

from .models import Post
from .forms import CustomUserRegistrationForm, UserProfileUpdateForm


class HomeView(TemplateView):
    template_name = 'blog/index.html'


class SignUpView(CreateView):
    form_class = CustomUserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


class LogInView(LoginView):
    template_name = 'registration/login.html'
    next_page = reverse_lazy('home')


class LogOutView(LogoutView):
    next_page = reverse_lazy('home')
    template_name = 'registration/logged_out.html'


class ProfileUpdateView(UpdateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    template_name = 'registration/profile.html'
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
    return render(request, 'registration/profile.html', context)


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListPostsView(ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-published_date')


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class DetailPostView(DetailView):
    model = Post
    context_object_name = 'post'


class UpdatePostView(UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('posts')

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
