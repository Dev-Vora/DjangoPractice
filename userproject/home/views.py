from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
# Create your views here.
#password Dev@@@111
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginUser(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
             return render(request, 'login.html')
    
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")