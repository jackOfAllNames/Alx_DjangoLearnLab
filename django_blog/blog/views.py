from django.db.models import Q
from taggit.forms import TagWidget
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DeleteView, DetailView

from .models import Post, Comment
from .forms import CustomUserRegistrationForm, UserProfileUpdateForm, CommentForm, PostForm


class HomeView(TemplateView):
    template_name = 'blog/index.html'


class SignUpView(CreateView):
    form_class = CustomUserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'blog/register.html'


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


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListPostsView(ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-published_date')
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(content__icontains=q) |
                Q(tags__name__icontains=q)
            ).distinct()
        return queryset
    

class PostByTagListView(ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug')
        return Post.objects.filter(tags__slug=tag_slug).order_by('-published_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.kwargs.get('tag_slug')
        return context


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


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def handle_no_permission(self):
        return redirect('posts')

    # def get_queryset(self):
    #     return Post.objects.filter(author=self.request.user)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['post_pk']
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs['post_pk'])
        return context
    
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.kwargs['post_pk']})
    

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = self.object.post
        return context
    
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('posts')

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})

    def handle_no_permission(self):
        return redirect('posts')


class CommentListView(ListView):
    model = Comment
    context_object_name = 'comments'

    def get_queryset(self):
        post_pk = self.kwargs.get('post_pk')
        return Comment.objects.filter(post_id=post_pk).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs['post_pk'])
        return context