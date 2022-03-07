from django.shortcuts import render,HttpResponse
from .import views
from home.models import Contact
from blog.models import Post
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'home/home.html')

def contact(request):
    if(request.method == 'POST'):
        name= request.POST['name']
        phone= request.POST['phone']
        email= request.POST['email']
        content= request.POST['content']
        print(name,email,content,phone)
        contact=Contact(name=name,phone=phone,email=email,content=content)
        contact.save()
        if len(name)<2 or len(email)<2 or len(phone)!=10 or len(content)<4:
            messages.error(request,'Sorry your messages is not delivered.Please fill it correctly.')
        else:
            contact=Contact(name=name,phone=phone,email=email,content=content)
            contact.save()
            messages.success(request,'Your message has been delivered succesfully.')
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')

def search(request):
    query=request.GET['query']
    allPosts= Post.objects.filter(title__icontains=query)
    params={'allPosts': allPosts}
    return render(request, 'home/search.html', params)