from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("my-login",views.my_login, name="my-login"),
    path("user_logout",views.user_logout, name="user_logout"),
    path("dashboard',", views.dashboard, name="dashboard"), 
    path("create-record",views.create_record, name="create-record"),
    path('update-record/<str:pk>/', views.update_record, name='update-record'),
    path('delete-record/<str:pk>/', views.delete_record, name='delete-record'),
]
   
