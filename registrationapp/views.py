from email import message
from django.forms import PasswordInput
from django.shortcuts import redirect, render
from .models import*

# Create your views here.

# To show the register page
def register(request):
    return render(request,"app/register.html")

#to show login page
def loginpage(request):
    return render(request,"app/login.html")  

#to Show forgotpassword page
def forgotpasswordpage(request):
    return render(request,"app/forgotpassword.html")

#To show updatepassword page
def updatepasswordpage(request):
    return render(request,"app/updatepassword.html")  

# Method to register the user
def UserRegister(request):
    if request.method == "POST":
       fname=request.POST['fname']
       lname=request.POST['lname']
       email=request.POST['email']
       contact=request.POST['contact']
       password=request.POST['password']
       cpassword=request.POST['cpassword']

       newuser = user.objects.filter(Email=email)

       if newuser:
            message = "user already exixts"
            return render(request,"app/register.html",{'msg':message})
       else:
           if password == cpassword:
              newuser=user.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password)

              return render(request,"app/login.html")
           else:
               message="password and confirm password does not match"
               return render(request,"app/register.html",{'msg':message})   

# Method to login the user
def Userlogin(request):
    if request.method == "POST":
        email=request.POST['email']
        password=request.POST['password']
        newuser = user.objects.get(Email=email) 
        if newuser:
            if newuser.Password==password:
                request.session['Firstname'] = newuser.Firstname
                request.session['Lastname'] = newuser.Lastname
                request.session['Email'] = newuser.Email
                return render(request,"app/home.html")
            else:
                message="Password does not match"
                return render(request,"app/login.html",{'msg':message})    

        else:
            message="Email id does not exist"
            return render(request,"app/register.html",{'msg':message})    

# Method to  Forget password
def newpassword(request):
    if request.method == "POST":
        email=request.POST['email'] 
        password=request.POST['password']
        cpassword=request.POST['cpassword']  
        userdata=user.objects.get(Email=email)
        if password==cpassword:
            userdata.Password=password
            userdata.save()
            return redirect('loginpage')
        else:
            message="Password and Confirm Password does not same"
            return render(request,"app/forgotpassword.html",{'msg':message})    

# Method to  update password
def updatepassword(request):
    if request.method == "POST":
        email=request.POST['email'] 
        password=request.POST['upassword']    
        userdata=user.objects.get(Email=email)
        userdata.Password=password
        userdata.save()
        message="password updated successfully"
        return render(request,"app/home.html",{'msg':message})
