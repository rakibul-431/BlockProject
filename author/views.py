from django.shortcuts import render,redirect
from author.form import RejistrationForm,Userdatachange
from django.contrib.auth import authenticate,update_session_auth_hash,login,logout
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.contrib.auth.views import LoginView,LogoutView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy


# Create your views here.

def UserRejistration(request):
    if request.method=='POST':
       register_form=RejistrationForm(request.POST)
       if register_form.is_valid():
           register_form.save()
           messages.success(request,'Your account creat successfull.')
           return redirect('rejisterpath')
    else:
        register_form=RejistrationForm()
    return render(request,'rejister.html',{'form':register_form,'type':'Rejisttration page'})



def UserLoginForm(request):
    if request.method=='POST':
      loginForm=AuthenticationForm(request=request,data=request.POST)
      if loginForm.is_valid():
          username=loginForm.cleaned_data['username']
          userpass=loginForm.cleaned_data['password']
          user=authenticate(username=username,password=userpass)
          if user is not None:
              messages.success(request,'You logged in successfully.')
              login(request,user)
              return redirect('Homepage')
          else:
              messages.warning(request,'Your logged information incorrect.')
              return redirect('rejisterpath')
    else:
        loginForm=AuthenticationForm()
    return render(request,'rejister.html',{'Form':loginForm,'type':'Login page'})
@login_required
def User_Data_change(request):
    if request.method=='POST':
       Userdatachange_form=Userdatachange(request.POST,instance=request)
       if Userdatachange_form.is_valid():
           Userdatachange_form.save()
           messages.success(request,'Your account creat successfull.')
           return redirect('Homepage')
    else:
       Userdatachange_form=Userdatachange(instance=request.user)
    return render(request,'update_data.html',{'Form':Userdatachange_form}) 
@login_required
def UserProfile(request):
     all_post=Post.objects.filter(author=request.user)
     return render(request,'profile.html',{'form':all_post})

@login_required
def pass_change(request):
    if request.method=='POST':
       Userpasschange_form=PasswordChangeForm(request.user,data=request.POST)
       if  Userpasschange_form.is_valid():
           Userpasschange_form.save()
           update_session_auth_hash(request,Userpasschange_form.user)
           messages.success(request,'Your update successfull.')
           return redirect('Homepage')
    else:
       Userpasschange_form=PasswordChangeForm(request.user)
    return render(request,'pass_change.html',{'Form':Userpasschange_form,'type':'User datachange form'}) 





@login_required
def log_out(request):
    logout(request) 
    return redirect('Homepage') 


#Class base View .....
class userlogin(LoginView):
    template_name='rejister.html'
    # success_url=reverse_lazy('author')
    def get_success_url(self):
        return reverse_lazy('userProfile')
    def form_valid(self, form):
        messages.success(self.request,'Login successfull.')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request,'Login information is incorrect.')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['type']='Login'
        return context

    

