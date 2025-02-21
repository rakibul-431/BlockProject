from django.shortcuts import render,redirect
from categories.form import CategoryForm

# Create your views here.

def add_category(request):
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_post')
    else:
      form=CategoryForm()
    return render(request,'add_categories.html',{'form':form})
