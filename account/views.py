from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth import authenticate,login
from .forms import AccountForm
from .models import Account

# Create your views here.
def signup(request):
    if request.method=='POST':
        form=AccountForm(request.POST or None)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            username=form.cleaned_data['email'].split('@')[0]  
            password=form.cleaned_data['password']
            user=Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password) 
            user.save()
            messages.success(request,'Sign Up successful !')
            return redirect('signin')

           
    else:
         form=AccountForm()

    context=dict(form=form)
    return render(request,'account/signup.html',context)

def signin(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password'] 
        user=authenticate(email=email,password=password)
        print(user)
        if user is not None:
            print('user is not none')
            login(request,user)
            messages.success(request,'sign In successful')
            return redirect('user_profile:profile_edit', username=request.user.username)
        else:
            print('errors')
            messages.error(request,'Invalid email or password')
            return redirect('signin')
        
    else:
     return render(request,'account/signin.html')


def signout(request):
    auth.logout(request)
    
    return redirect('home')


def home(request):
    return render(request,'account/home.html')