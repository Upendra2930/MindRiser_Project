from rest_framework import serializers
from home.models import Contact, FeedBack, UserInfo

class ContactSerializer(serializers.ModelSerializer):
    class Meta:

        model = Contact
        fields = ( "name", "email", "phone", "desc" ,)
      

class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = ( "name","email", "age", "desc")
       
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = [ 'name','gender', 'email', 'age', 'address','occupation']       