from django.urls import path
# from .views import ContactApiView
from helloapi import views
urlpatterns = [
    # path('home/', ContactApiView.as_view())
    path('contact', views.Contact_list),
    path('user', views.User_Info),
    path('user/<str:user>', views.user_detail),
]
