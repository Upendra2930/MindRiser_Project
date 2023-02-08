from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [ 
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("email", views.email, name='email'),
    path("Contact",views.contact,name='contact'),
    path("feedback",views.feedback,name='feedback'),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('user',views.userinfo, name="user"),
    

]

    



  
