from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from rest_framework import routers
from candydendy import views
from candydendy.views import CandyViewSet, CandyViewSetFree


urlpatterns = [
    path('', views.home, name='home'),
    path('', include('django_prometheus.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='form/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='form/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('candyfree/', views.candyfree, name='candyfree'),
    path('candy/', views.candy, name='candy'),
    path('api', CandyViewSet.as_view()),
    path('api/free', CandyViewSetFree.as_view()),
]
