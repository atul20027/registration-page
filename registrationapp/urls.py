from unicodedata import name
from django.urls import path,include
from .import views
urlpatterns = [
 path("",views.register,name="registerpage"),
 path("loginpage/",views.loginpage,name="loginpage"),
 path("forgotpasswordpage/",views.forgotpasswordpage,name="forgotpasswordpage"),
 path("updatepasswordpage/",views.updatepasswordpage,name="updatepasswordpage"),
 path("register/",views.UserRegister,name="register"),
 path("login/",views.Userlogin,name="login"), 
 path("resetpassword/",views.newpassword,name="resetpassword"), # it will do forgot password
 path("updatepassword/",views.updatepassword,name="updatepassword"), #it will update password after login
 
]
