from django.shortcuts import render,redirect
from django.contrib import messages,auth
from .forms import AccountForm,SigninForm

# Create your views here.
def signup(request):
    if request.method=='POST':
        form=AccountForm(request.POST or None)
        if form.is_valid():
              
            password=form.cleaned_data['password']
            confirm_password=form.cleaned_data['confirm_password']
            if password!=confirm_password:
                messages.error(request,'"password" and "confirm password" does not match')
            else:    
                form.save()

           
    else:
         form=AccountForm()

    context=dict(form=form)
    return render(request,'account/signup.html',context)

def signin(request):
    if request.method=="POST":
        form=SigninForm(request.POST or None)
        if form.is_valid():
             email=form.cleaned_data['email']
             password=form.cleaned_data['password']
             user=auth.authenticate(email=email,password=password)
             if user is not None:
                  auth.login(request,user)
                  messages.success(request,'signin successful')
                  return redirect('profile')
             else:
                  messages.error(request,'Invalid email or password')
                  return redirect('signin')
    else:
         form=SigninForm()
    context=dict(form=form)
    return render(request,'account/signin.html',context)


def signout(request):
    auth.logout(request)
    
    return redirect('signin')