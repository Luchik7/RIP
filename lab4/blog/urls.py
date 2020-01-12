from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    url(r'^registration/', views.registration, name='registration'),
    url(r'^login/', views.LoginForm.as_view(), name='login'),
    url(r'^profile/', views.user_profile, name='profile'),
    url(r'^logout/', views.LogoutForm.as_view(), name='logout'),
]