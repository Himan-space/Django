from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from students.models import Student_Details
from .forms import StudentForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request=request,
                template_name='home_page/home.html')

@login_required(login_url='/login/')
def student(request):
    return render(request=request,
                template_name='home_page/home.html')

def signup(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        studentform=StudentForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            username=User.objects.get(id=request.user.id)
            
            messages.success(request, "New Account Created: %s" %username )
            if studentform.is_valid():
                print(username)
            else:
                Student_Details.objects.create(Username=username,**studentform.cleaned_data)
            return redirect(student)
        else:
            for msg in form.error_messages:
                messages.error(request,f"{msg}:{form.error_messages[msg]}")
    form=UserCreationForm
    studentform=StudentForm
    # if request.user.is_authenticated:
    #     return redirect(student)
    return render(request=request,
                template_name='home_page/signup.html',
                context={"form":form,"studentform":studentform})


def login_req(request):   
    if request.method=="POST":
        form1 = AuthenticationForm(request,data=request.POST)
        if form1.is_valid():   
            username1=form1.cleaned_data.get('username')
            password1=form1.cleaned_data.get('password')        
            user1=authenticate(username=username1,password=password1)
            login(request,user1)
            messages.info(request,"You are logged in as %s"%username1)
            return redirect(student)
        else:
            messages.error(request,"Invalid Username or Password")
    
    form1=AuthenticationForm
    # if request.user.is_authenticated:
    #     return redirect(student)
    return render(request,'home_page/login.html',{'form1':form1})


def logout_req(request):
    logout(request)
    messages.info(request,"Logged out Successfully")
    return redirect(home)

