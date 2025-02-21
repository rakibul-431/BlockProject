from django.shortcuts import render,redirect
from author.form import AuthorForm

# Create your views here.

def add_author(request):
    if request.method=='POST':
       form=AuthorForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('authorpath')
    else:
     form=AuthorForm()
    return render(request,'add_author.html',{'form':form})

