from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'DCBSapp'

urlpatterns = [

    path('', views.home, name = 'home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]