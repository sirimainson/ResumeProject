from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login

def login_view(request):
    return render(request, 'AuthenApp/login.html')

def logout_view(request):
    logout(request)
    return redirect('/')
    
def authen_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    print(user)
    if user is not None:
        login(request, user)
        return redirect('index')
    else:
        return login_view(request)
