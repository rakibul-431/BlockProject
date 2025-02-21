from django.shortcuts import render,redirect
from posts.form import PostForm
from posts.models import Post
# Create your views here.
def add_post(request):
    if request.method=='POST':
         form=PostForm(request.POST)
         if form.is_valid():
              form.save()
              return redirect('all_post')
    else:
      form=PostForm()
    return render(request,'add_post.html',{'form':form})

def Show_allBlocg(request):
    allBlocg=Post.objects.all()
    return render(request,'show_all_blog.html',{'bl':allBlocg})

def Edit(request,id):
       post=Post.objects.get(pk=id)
       if request.method=='POST':
            form=PostForm(request.POST,instance=post)
            if form.is_valid():
                 form.save()
                 return redirect('all_post')
       else:
         form=PostForm(instance=post)
       return render(request,'edit.html',{'form':form})
def Delete(request,id):
    post=Post.objects.get(pk=id).delete()
    return redirect('all_post')
       
