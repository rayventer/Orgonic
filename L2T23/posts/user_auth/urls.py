from django.urls import path, include
from . import views
app_name = 'user_auth'
urlpatterns = [
    path('', views.loginpage, name='login'),
    path('register/', views.user_registration, name='register'),
    path('register_user/', views.register_user, name ='register_user'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('create_post/', views.create_post, name='create_post'),
    path('poster/', views.poster, name='poster'),
    path('viewPosts/', views.viewposts, name='viewPosts'),
    path('home/', views.index, name='home' )
]