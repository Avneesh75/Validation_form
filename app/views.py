from email import message
from django.forms import PasswordInput
from django.shortcuts import render
from .models import User

# Create your views here.

def Register(request):
    return render(request,"register.html")


# View for user register
def UserRegister(request):
    if request.method =="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        #First we will validate that user already exist
        user = User.objects.filter(Email=email)

        if user:
            message = "User already exist"
            return render(request,'register.html',{'msg':message})

        else:
            if password==cpassword:
                newuser = User.objects.create(Firstname=fname,
                                                Lastname=lname,
                                                Email=email,
                                                Contact=contact,
                                                Password=password)
                message = "User register Sucessfully..."
                return render(request,'login.html',{'msg':message})
            else:
                message = "Password and Confirm Password Doesnot Match"
                return render(request,'register.html',{'msg':message})


def Login(request):
    return render(request,'login.html')

#login user
def LoginUser(request):
    if request.method =="POST":
        email = request.POST['email']
        password = request.POST['password']
        #print(email)
        #print(password)
        #checking the email id with database
        user = User.objects.get(Email=email)

        if user:
            if user.Password==password:
                # we are getting user data in session
                request.session['Firstname']= user.Firstname
                request.session['Lastname']= user.Lastname
                request.session['Email']= user.Email
                return render(request,'home.html')
            else:
                message = "Password Does not exist"
                return render(request,'login.html',{'msg':message})
    else:
        message = "User does not Exist"
        return render(request,'register.html',{'msg':message})

