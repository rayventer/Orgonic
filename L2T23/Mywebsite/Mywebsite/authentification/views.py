from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def user_registration(request):
    return render(request, 'authentication/createuser.html')

def register_user(request):
    username1 = request.POST.get('username')
    password1 = request.POST.get('password')
    user =User.objects.create(username=username1, password=password1)
    user.set_password(password1)
    user.is_active=True
    user.save()
    return HttpResponseRedirect(
        reverse('authentication:login')
        )
    


def user_login(request):
    return render(request, 'authentication/login.html')


def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })


def authenticate_user(request):
    username1 = request.POST['username']
    password1 = request.POST['password']
    user = authenticate(username=username1, password=password1)
    if user is None:
        return HttpResponseRedirect(
            reverse('authentication:login')
    )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('authentication:show_user'))

def logged(request):
    if request.user.isauthenticated == True:
        return True
    

# Create your views here.
