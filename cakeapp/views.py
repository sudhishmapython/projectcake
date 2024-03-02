from django.contrib import messages
from django.shortcuts import render, redirect
from cakeapp.forms import LoginRegister,Ownerform,Userform

# Create your views here.
def index(request):
    return render(request,'index1.html')

def owner_registration(request):
    login_form=LoginRegister()
    owner_form=Ownerform()
    if request.method=='POST':
        login_form=LoginRegister(request.POST)
        owner_form=Ownerform(request.POST)
        if login_form.is_valid() and owner_form.is_valid():
            user=login_form.save(commit=False)
            user.is_owner=True
            user.save()
            owner=owner_form.save(commit=False)
            owner.user=user
            owner.save()
            messages.info(request,'register successfully')
            return redirect('login_view')
    return render(request,'owner_reg.html',{'login_form':login_form,'owner_form':owner_form})



def user_registration(request):
    login_form=LoginRegister()
    user_form=Userform()
    if request.method=='POST':
        login_form=LoginRegister(request.POST)
        user_form=Userform(request.POST)
        if login_form.is_valid() and user_form.is_valid():
            user=login_form.save(commit=False)
            user.is_user=True
            user.save()
            user=user_form.save(commit=False)
            user.user=user
            user.save()
            messages.info(request,'register successfully')
            return redirect('login_view')
    return render(request,'user_reg.html',{'login_form':login_form,'user_form':user_form})



def login(request):
    return render(request, 'login.html')
