from django.contrib import admin
from django.urls import path, include
from home import views
# For the get request there shoukd be  / after the url pattern.
# For the post request there should not be any / after the url pattern
urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('search', views.search, name="search"),
]