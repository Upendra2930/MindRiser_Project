from django.contrib import admin
from home.models import Contact
from home.models import FeedBack, UserInfo, Order

# Register your models here.



admin.site.register(Contact)
admin.site.register(FeedBack)
admin.site.register(UserInfo)
admin.site.register(Order)

