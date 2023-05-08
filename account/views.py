from django.shortcuts import render
from .forms import AccountForm

# Create your views here.
def signup(request):
    if request.method=='POST':
        form=AccountForm(request.POST or None)
        if form.is_valid():
            form.save()

    else:
         form=AccountForm()

    context=dict(form=form)
    return render(request,'account/signup.html',context)

def signin(request):
    context=dict()
    return render(request,'account/signin.html',context)


def signout(request):
    context=dict()
    return render(request,'account/signout.html',context)