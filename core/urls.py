from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register_user/', views.register_user, name='register_user'),
    path('logout/', views.logout, name='logout'),
    
]