from django.urls import path,include
from .import views

urlpatterns = [

    path("",views.Register,name="register"),
    path("register/",views.UserRegister,name='register'),
    path("login/",views.Login,name='login'),
    path("loginuser/",views.LoginUser,name="loginuser")
]
