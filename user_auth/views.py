from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from posts.views import index
#used to view all posts
def viewposts(request):
    latest_post = Post.objects.all()
    context = {'latest_post': latest_post}
    return render(request, "post.html", context)

def loginpage(request):
    return render(request, "login.html")


def index(request):
    return render(request, "index.html")

# Create your views here.
def user_registration(request):
    return render(request, 'authentication/register.html')
#used to register a user
def register_user(request):
    try:
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        user =User.objects.create(username=username1, password=password1)
        user.set_password(password1)
        user.is_active=True
        user.save()
        return HttpResponseRedirect(
            reverse('user_auth:login')
            )
    except Exception:
        HttpResponse('incorrect sign in attempt')
#goes to post page
def poster(request):
    return render(request,'create_post.html')

#used to authenticate a user
def authenticate_user(request):
    username1 = request.POST['username']
    password1 = request.POST['password']
    user = authenticate(username=username1, password=password1)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
    )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:home'))

#used to create a post and redirects if you arent logged in
@login_required(login_url='user_auth:login')
def create_post(request):
    Title = request.POST.get('title')
    Content = request.POST.get('content')
    newPost= Post.create(Title, Content)
    return HttpResponseRedirect(
            reverse('user_auth:home')
    )