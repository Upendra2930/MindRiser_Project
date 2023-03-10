from django.db import models

# Create your models here.
class Contact(models.Model):
    name =models.CharField(max_length=122)
    email =models.CharField(max_length=122)
    phone =models.CharField(max_length=12)
    desc =models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
   
class FeedBack(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    age = models.CharField(max_length=12)
    desc= models.TextField()
    def __str__(self):
        return self.name

class UserInfo(models.Model):
    name = models.CharField(max_length=122)
    gender = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    age = models.CharField(max_length=12)
    address = models.CharField(max_length=122)
    occupation = models.CharField(max_length=122)
    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    item = models.CharField(max_length=122)
    item_no = models.CharField(max_length=5)
    address = models.CharField(max_length=50)       
    def __str__(self):
        return self.name