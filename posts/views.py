from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from posts.form import PostForm,CommentForm
from posts.models import Post,comment
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView,DeleteView,DetailView
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormMixin
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



#Class based View from here.
@method_decorator(login_required,name='dispatch')
class addpost(CreateView):
    model=Post
    form_class=PostForm
    template_name='add_post.html'
    success_url=reverse_lazy('userProfile')
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
@method_decorator(login_required,name='dispatch')    
class Editview( UpdateView):
    model=Post
    form_class=PostForm
    template_name='edit.html'
    success_url=reverse_lazy('userProfile')
    pk_url_kwarg ='id'

@method_decorator(login_required,name='dispatch')
class userDeleteView(DeleteView):
        model=Post
        template_name='delete.html'
        success_url=reverse_lazy('userProfile')
        pk_url_kwarg='id'
class postDetail(FormMixin,DetailView):
     model=Post
     template_name='postDetail.html'
     pk_url_kwarg='id'
    #  context_object_name = 'post'
     form_class=CommentForm

     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['comments'] = self.object.comment.all()  # Fetch all comments related to this post
          context['form'] = self.get_form()
          return context
     
     def post(self, request, *args, **kwargs):
        """Handles form submission for comments."""
        self.object = self.get_object()  # Get the post object
        form = self.get_form()

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object  # Link the comment to the post
            comment.save()
            return redirect('postview', id=self.object.pk)  # Reload the page

        return self.render_to_response(self.get_context_data(form=form))

    #  def get_context_data(self,**kwargs):
    #       context=super.get_context_data(**kwargs)


    #comment bt Function 
   
    # def post_detail(request, pk):
    # post = get_object_or_404(Post, pk=pk)
    # comments = post.comments.all()  # Fetch all comments related to this post
    # form = CommentForm()

    # if request.method == "POST":
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.post = post  # Link comment to the current post
    #         comment.save()
    #         return redirect('post_detail', pk=post.pk)  # Reload the page after comment submission

    # return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})
             
          
