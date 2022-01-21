from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('blank')
        else:
            messages.info(request,'invalid login')
            return redirect('login')

    return  render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['password1']
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email alrdy taken taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save();


        else:
            messages.info(request,'password not matching')
            return redirect('register')
        print('user created')
        return redirect('login')
    return render(request,'register.html')
def blank(request):
    return render(request,'reg.html')


def booking(request):
    if request.method=='POST':
        username=request.POST['username']
        Gender = request.POST['Gender']
        Year_of_Birth = request.POST['Year_of_Birth']
        Age = request.POST['Age']
        Address = request.POST['Address']
        Mobile = request.POST['Mobile']
        District = request.POST['District']
        user = User.objects.create_user(username=username, Gender=Gender, Year_of_Birth=Year_of_Birth,
                                            Age=Age, Address=Address,Mobile=Mobile,District=District)
        user.save()

        return redirect('submit12')

    return render(request,'booking1.html')


def submit12(request):
    return render(request,'submit.html')

def exit(request):
    return render(request,'exit.html')
