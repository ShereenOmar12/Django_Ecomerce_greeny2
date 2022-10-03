from django.shortcuts import render
from .forms import SignupForm

# Create your views here.
def signup (request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            myform = form.save(commit=False)

            profile = Profile.objects.get(user__username=username)
            profile.active = False
            profile.save()


    else:
        form = SignupForm()    
    return render (request,'registration/signup.html',{'form':form})    