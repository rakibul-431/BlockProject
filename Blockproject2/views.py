from django.shortcuts import render,redirect
from posts.models import Post
from categories.models import Category

def Show_allPost(request,category_slug=None):
    postData=Post.objects.all()
    if category_slug is not None:
        category=Category.objects.get(slug=category_slug)
        postData=Post.objects.filter(category=category)
    categoryData=Category.objects.all()
    return render(request,'Home.html',{'postdata':postData,'categorydata':categoryData})