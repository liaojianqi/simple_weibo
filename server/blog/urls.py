from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_blog, name='create'),
    path('delete', views.delete_blog, name='delete'),
    path('list', views.list_blog, name='list'),
]
