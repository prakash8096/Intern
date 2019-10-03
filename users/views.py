from django.shortcuts import render,redirect
from .forms import Forms,UserModify,ProfileUpdate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def basefile(request):
    return render(request,'base.html')

def register(request):
    if request.method=="POST":
        form=Forms(request.POST)

        if form.is_valid():

            form.save()

            username=form.cleaned_data.get('username')
            messages.success(request,f'Your Registration was sucessful now you can Login!')
            
            return redirect('login')


    form=Forms()
    return render(request,'register.html',{'form':form})
def home(request):
    return render(request,'home.html')


@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserModify(request.POST,instance=request.user)
        p_form=ProfileUpdate(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
    else:

        u_form=UserModify(instance=request.user)
        p_form=ProfileUpdate(instance=request.user.profile)


    context={'u_form':u_form,'p_form':p_form}
    return render(request,'profile.html',context)