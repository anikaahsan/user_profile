from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

# Create your views here.
@login_required
def profile_view(request):
    if request.method=="POST":
        form=ProfileForm(request.POST or None,request.FILES)
        if form.is_valid():
            form.save()
            
    else:
        form=ProfileForm()        



    context=dict(form=form)
    return render(request,'user_profile/profile.html',context)