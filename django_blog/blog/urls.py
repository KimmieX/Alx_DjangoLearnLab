from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from .views import add_comment, CommentUpdateView, CommentDeleteView, CommentCreateView
from .views import (PostListView, PostDetailView,PostCreateView, PostUpdateView, PostDeleteView)
from .views import CommentCreateView



urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:post_id>/comments/new/', add_comment, name='comment-add'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-add'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-add'),

]