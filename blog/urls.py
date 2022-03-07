from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.blogHome,name='home'),
    path('<str:slug>/',views.blogPost,name='blogpost'),
]   
# The second blog will be included to the same