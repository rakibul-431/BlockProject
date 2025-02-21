from django.shortcuts import render,redirect
from profiles.form import ProfileForm
# Create your views here.

def Add_profile(request):
    if request.method=='POST':
        form=ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_post')
    else: 
      form=ProfileForm()
    return render(request,'add_profiles.html',{'form':form})