from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    customers = Customer.objects.all()
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
        return render(request,'index.html', {'customers': customers})
    
def logout(request):
    auth.logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('index')

@login_required(login_url='index')
def customer_record(request,pk):
    record = Customer.objects.get(id=pk)
    return render(request,'record.html',{'record': record})

@login_required(login_url='index')
def delete_record(request,pk):
    record = Customer.objects.get(id=pk)
    record.delete()
    messages.success(request,"Record deleted successfully..")
    return redirect('index')

@login_required(login_url='index')
def add_record(request):
    if request.method == "POST":
        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Record Added")
            return redirect('index')
    else:
        form = AddRecordForm()
    return render(request,'add_record.html',{'form':form})


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