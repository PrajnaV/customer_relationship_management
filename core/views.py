from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def index(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)   #checks if the user already registered in database

        if user is not None:    #if user exists
            auth.login(request,user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('index')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        return render(request,'index.html')
    
def logout(request):
    auth.logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('index')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
			# Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form':form})