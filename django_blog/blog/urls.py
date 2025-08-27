from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('', include('blog.urls')),
]