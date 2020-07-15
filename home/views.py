from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import user_contact
from django.contrib import messages
import sqlite3
from Blog.models import blogpost
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def index(request):
    val=blogpost.objects.all()
    content={'allposts':val}
    return render(request,'home/home.html',content)
def contact(request):
    
    if request.method=="POST":
        print("inside")
        fname=request.POST.get("Firstname")+" "+request.POST.get("lastname")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        print(fname,email,phone)
        if len(fname)<2 or len(email)<4 or len(phone)<10:
            messages.error(request,'Please fill the form correctly.')
        else:
            try:
                val=user_contact(name=fname,email=email,phone=phone,num=100)
                val.save()
                messages.success(request,'Thank you! We will get in touch with you soon.')
            except Exception as e:
                messages.error(request,'Database Error')
       

    return render(request,'home/contact.html')
    
def about(request):
    return render(request,'home/aboutus.html')


def data(request):

    val=user_contact.objects.raw('Select sno,name,email,phone from home_user_contact')
    for x in val:
        print(x)
    return render(request,'home/data.html')

def createuser(request):
    if request.method=="POST":
        username=request.POST.get("fname")+" "+request.POST.get("lname")
        email=request.POST.get("email")
        
        password=request.POST.get("pwd")
        val=User.objects.create_user(username=username ,email=email,password=password)
        val.first_name=request.POST.get("fname")
        val.last_name=request.POST.get("lname")
        val.save()
        messages.success(request,'User created Succesfully.')
        return redirect('/')
    else:
        return HttpResponse("Error-404 Not Found")

def handlelogout(request):
    logout(request)
    messages.success(request,'User logged Out Succesfully.')
    return redirect('home')

def handlelogin(request):
    print("handlelogin")
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("loginpwd")
        print(username,password)
        user=authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,'User logged in  Succesfully.')
            return redirect('/')
        else:
            messages.error(request,'User Authentication Failed.')
            return redirect('/')

    else:
        return HttpResponse('Error 404- Forbidden Access')
