from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.


def  index(request):
    
    return render(request,'index.html')

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        
        user = authenticate(request=request,username=username,password=password)
        
        if user != None:
            auth_login(request,user)
            
            return render(request,'index.html')
            
    return render(request,"login.html")

def register(request):
    
    if request.method == 'POST':
        
        username = request.POST['username']
        email = request.POST['email']
        role = request.POST.get('role')
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        
        if password != confirmPassword:
            
            messages.error(request,"Passwords don't Match ")
            
            return redirect(register)
        
        try: 
            validate_email(email)
        
        except ValidationError:
            messages.error(request,"Invalid Email")
            return redirect(register)
        
            
          # Check for existing email or username
        if User.objects.filter(email=email).first():
            messages.error(request,"Email exists")
            return redirect(register)
        if User.objects.filter(username=username).first():
            messages.error(request,"Username exist")
            return redirect(register)
        
        # Create user
        try: 
            user = User.objects.create(username=username,email=email,password=password)
            user.save()
            # Authenticate and login user
            
            try:
                user_login = authenticate(request,username=username,password=password)
                
                if user_login is not None:
                    auth_login(request,user_login)
                    
            except:
                messages.error(request,"Authentication Falied Try Again ")
                
                user.delete()
                
                return redirect(register)

            # Create Profile for user
            try:
                Profile.objects.create(user=user,personality=role).save()
                
            except Exception as e:
                messages.error(request,f"error creating Profile {e}")
                
                user.delete()
                
                return redirect(register)
                
            return render(request,'profile.html')
        
        except Exception as e:
            messages.error(request,f"error creating user {e}")
            
            return redirect('register')
        
        
          # Redirect to Profile page
            
        
    
    return render(request,'register.html')

def logOut(request):
    
    auth_logout(request=request)
    
    return redirect(login)


