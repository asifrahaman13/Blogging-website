from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.blogHome,name='home'),
    path('postComment', views.postComment, name="postComment"),
    path('<str:slug>/',views.blogPost,name='blogpost'),
    # path('postComment', views.postComment, name="postComment"),
]   
# The second blog will be included to the same