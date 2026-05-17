from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate


# views.py
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout

# Create your views here.

def index(request):
    return render(request, "users/index.html")
def login(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        User = authenticate(request, username=username, password=password)
        if User is not None:
            auth_login(request, User)
            return redirect("tasksapp:index")
        
        else:
            context = {'message': "Invalid username or password please try again or register if you don't have an account"}
            return render(request, 'users/login.html', context)
    return render(request, "users/login.html")    
    


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)  
            return render(request, "users/login.html", {
                "message": "Registration successful, you can now login"
            })
        else:
            context = {"message": "Username already exists, please choose a different username or login if you already have an account"}
            return render(request, 'users/register.html', context)
    
    return render(request, "users/register.html")
def logout(request):
    auth_logout(request)
    return redirect("users:login")