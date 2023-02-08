from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact, UserInfo
from home.models import FeedBack
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout




# Create your views here.
def index(request):
    if request.user.is_anonymous:

        return redirect("/login") 
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
         

            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, 'login.html')        
   

def logoutUser(request):
    logout(request)
    return redirect("/login")

def email(request):
    return render(request, 'email.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc= request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()     

        
        messages.success(request, 'Your message has been sent!')
    else:
        print("Sorry, please input a correct data!!!!")    
    return render(request, 'Contact.html')    


def feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        desc = request.POST.get('desc')
        feedback = FeedBack (name=name,email=email,age=age,desc=desc)
        feedback.save()

        messages.success(request, 'Your FeedBack has been send!!')
    return render(request, 'feedback.html')   


def userinfo(request):
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        age = request.POST.get('age')
        address = request.POST.get('address')
        occupation = request.POST.get('occupation')
        userinfo = UserInfo (name=name,gender=gender,email=email,age=age,address=address,occupation=occupation)
        userinfo.save()

        messages.success(request, 'Your Information has been send!!')
    return render(request, 'user.html')  
