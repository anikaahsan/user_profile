from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from.models import Profile
# Create your views here.
@login_required
def profile_create(request,username):
    profile=Profile.objects.get(user__username=username)
    if request.user.email == profile.user.email:
        if request.method=="POST":
            form=ProfileForm(request.POST or None,request.FILES ,instance=profile)
            if form.is_valid():
                form.save()
                return redirect('user_profile:profile_view' ,username=request.user.username)
                
        else:
           
            form=ProfileForm(instance=profile)        



        context=dict(form=form)
        return render(request,'user_profile/profile.html',context)
    else:
        return render(request,'restriction.html')

@login_required
def profile_view(request,username):
    profile=Profile.objects.get(user__username=username)


    context=dict(profile=profile)
    return render(request,'user_profile/profile_view.html',context)

