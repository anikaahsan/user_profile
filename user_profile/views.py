from django.shortcuts import render
from .forms import ProfileForm

# Create your views here.
def profile_view(request):
    if request.method=="POST":
        form=ProfileForm(request.POST or None,request.Files)
        if form.is_valid():
            form.save()
            
    else:
        form=ProfileForm()        



    context=dict(form=form)
    return render(request,'user_profile/profile.html',context)