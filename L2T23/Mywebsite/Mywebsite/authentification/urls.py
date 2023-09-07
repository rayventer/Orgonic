from django.urls import path, include
from . import views
app_name = 'authentification'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('registration/', views.user_registration, name='register'),
    path('register_user/', views.register_user, name ='register_user'),
    path('show_user/', views.show_user, name='show_user'),
    path('authenticate_user/', views.authenticate_user,
name='authenticate_user'),
    path('logged/', views.logged, name='logged')
]