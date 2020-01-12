from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView

from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class RegistrationForm(forms.Form):
   username = forms.CharField(min_length=5, label='Логин')
   password = forms.CharField(min_length=6, widget=forms.PasswordInput, label='Пароль')
   password2 = forms.CharField(min_length=6, widget=forms.PasswordInput, label='Повторите ввод')

class LoginForm(AuthenticationForm):
    pass