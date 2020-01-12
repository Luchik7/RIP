from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.forms import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import FormView, View
from .models import *
from django.shortcuts import render, get_object_or_404
from blog.forms import *


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def registration(request):
   errors = []
   if request.method == 'POST':
       username = request.POST.get('username')
       if not username:
           errors.append('Введите логин')
       elif len(username) < 5:
           errors.append('Логин должен привышать 5 символов')

       password = request.POST.get('password')
       if not password:
           errors.append('Введите пароль')
       elif len(password) < 6:
           errors.append('Длинна пароля должна превышать 6 символов')
       password_repeat = request.POST.get('password2')

       if password != password_repeat:
           errors.append('Пароли должны совпадать')

       if not errors:
           return HttpResponseRedirect('blog/login/')

   return render(request, 'blog/registration.html', {'errors': errors})


class LoginForm(FormView):
    form_class = LoginForm
    success_url = "blog/profile/"
    template_name = "blog/login.html"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginForm, self).form_valid(form)


@login_required(login_url='/login/')
def user_profile(request):
    return render(request, 'blog/profile.html')

def get(request):
    logout(request)
    return HttpResponseRedirect("/")

class LogoutForm(View):
    pass


