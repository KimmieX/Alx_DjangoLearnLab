from django.urls import path
from .views import RegisterView, LoginView
from .views import follow_user, unfollow_user
from .views import FollowUserView, UnfollowUserView
from .views import FeedView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),    
    path('follow/<int:user_id>/', follow_user),
    path('unfollow/<int:user_id>/', unfollow_user),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('feed/', FeedView.as_view(), name='user-feed'),
]




