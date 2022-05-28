
from django.urls import path
from django.contrib import admin
from . import views
from django.contrib import admin
from django.urls import path

# from .views import *
  
urlpatterns = [
    
    path('',views.Home,name='App1fun'),
    path('allCriminals/', views.allCriminals, name="allCriminals"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.handleLogin, name='login'),
    path('logout/', views.handleLogout, name='logout'),
    path('about/', views.about, name='about'),
    path('viewCriminal/<int:crim_id>', views.viewCriminal, name="viewCriminal"),
    path('edit/<int:crim_id>', views.edit, name="edit"),
    path('deleteCriminal/<int:crim_id>', views.deleteCriminal, name="delete"),
    path('<slug:slug>/', views.notFound, name='notFound'),
]
