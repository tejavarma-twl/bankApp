from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import UserAccount

# Create your views here.

def signup(request):
    if request.POST:
        print(request.POST)
        fname       = request.POST.get('fname',False)
        lname       = request.POST.get('lname',False)
        username    = request.POST.get('username',False)
        email       = request.POST['email']
        password    = request.POST['password']
        user = User.objects.create_user(username, email, password, first_name=fname, last_name=lname)
        user.save()
        phone       = request.POST.get('phone')
        dob         = request.POST.get('dob')
        address     = request.POST.get('address')
        bank        = request.POST.get('bank')
        UserAccount.objects.create(user_id=user.id,phone=phone,dob=dob,address=address,bank=bank)
        return redirect(home)
    return render(request,'signup.html',{})

def home(request):
    if request.POST:
        print(request.POST)
        username       = request.POST.get('username',False)
        password       = request.POST.get('password',False)
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect(dashboard)
        else:
            pass
            # No backend authenticated the credentials
    return render(request,'login.html',{})

def dashboard(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect(home)
    return render(request,'index.html',{})

def transactions(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect(home)
    return render(request,'transactions.html',{})

def user_logout():
    logout(request)
    return redirect(home)

def transaction(request):
    return render(request,'login.html',{})