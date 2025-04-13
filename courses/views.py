from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout

# Create your views here.


def  index(request):
    
    return render(request,'index.html')

def login(request):
    
    print(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        
        user = authenticate(request=request,username=username,password=password)
        
        print(f"###########{user}")
        
        if user != None:
            auth_login(request,user)
            
            return render(request,'index.html')
            
    return render(request,"login.html")

def register(request):
    pass

def logOut(request):
    
    auth_logout(request=request)
    
    
    return HttpResponse("You've logged Out Successfully. ")


