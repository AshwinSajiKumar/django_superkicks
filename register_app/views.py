from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        repeatpassword=request.POST.get('repeatpassword')
        if password == repeatpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is Already Taken")
                return redirect('http://127.0.0.1:8000/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email is Already Taken")
                return redirect('http://127.0.0.1:8000/register/')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save()
                print("User is Created")
                return redirect("/")
        else:
            messages.info(request,"Password not Matching")
            return redirect('http://127.0.0.1:8000/register/')
        
    else:
        return render(request,"register.html")

def signin(request):
      if request.method=="POST":
          username=request.POST.get("username")
          password=request.POST.get("password")
          user=auth.authenticate(username=username,password=password)
          if user is not None:
              auth.login(request,user)
              return redirect("/")
          else:
              messages.info(request,"User does not exist")
              return redirect("http://127.0.0.1:8000/register/")
      else:
          return render(request,"signin.html")
      
def signout(request):
    auth.logout(request)
    return redirect("/")
