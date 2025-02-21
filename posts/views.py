from django.shortcuts import render,redirect
from posts.form import PostForm
from posts.models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_post(request):
    if request.method=='POST':
         form=PostForm(request.POST)
         if form.is_valid():
              form.instance.author=request.user
              form.save()
              return redirect('userProfile')
    else:
      form=PostForm()
    return render(request,'add_post.html',{'form':form})

@login_required
def Edit(request,id):
       post=Post.objects.get(pk=id)
       if request.method=='POST':
            form=PostForm(request.POST,instance=post)
            if form.is_valid():
                 form.instance.author=request.user
                 form.save()
                 return redirect('userProfile')
       else:
         form=PostForm(instance=post)
       return render(request,'edit.html',{'form':form})
@login_required
def Delete(request,id):
    Post.objects.get(pk=id).delete()
    return redirect('userProfile')
       
