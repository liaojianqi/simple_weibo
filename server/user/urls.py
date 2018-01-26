from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('follow', views.follow, name='follow'),
    path('cancel_follow', views.cancel_follow, name='cancel_follow'),
    path('follow_list', views.follow_list, name='follow_list'),
    path('follower_list', views.follower_list, name='follower_list'),
]