from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def Homepage(request):
    return render (request, 'home.html')
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("your password and confirm password is not same")
        else:
          my_user=User.objects.create_user(uname,email,pass1)
          my_user.save()
          return render (request, 'index.html')

    return render (request, 'signup.html')
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse("wrong password")
    return render (request, 'login.html')
def Index(request):
    return render(request, 'index.html')
def Logout(request):
    return render(request, 'login.html')
def Aboutpage(request):
    return render(request,'about.html')
def Book1(request):
    return render(request,'book1.html')