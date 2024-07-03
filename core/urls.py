from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register_user/', views.register_user, name='register_user'),
    path('logout/', views.logout, name='logout'),
    path('customer_record/<int:pk>',views.customer_record,name='customer_record'),
    path('delete_record/<int:pk>',views.delete_record,name='delete_record')
    
]