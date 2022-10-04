from django.shortcuts import render
from django.core.mail import send_mail

from .forms import SignupForm , UserActivateForm

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



            # send email
            send_mail(
                subject="Activate Your Account",
                message=f"use this code {profile.code} to activate your account",
                from_email = "oshereen19@gmail.com",
                recipient_list= [email],
                fail_silently = False
            )
            return redirect(f'/accounts/{username}/activate')


    else:
        form = SignupForm()    
    return render (request,'registration/signup.html',{'form':form}) 

def user_activate(request,username):
    if request.method == 'POST':
        form = UserActivateForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if profile.code == code:
                profile.activate=True
                profile.code=''
                profile.code_used=True
                return redirect('/accounts/login')  


    else:
        form= UserActivateForm()
    return render(request,'registration/activation.html',{'form':form})             