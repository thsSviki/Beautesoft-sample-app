from django.db import models

class App_req(models.Model):
    customer_n=models.CharField(max_length=100)
    #customer_area=models.CharField(max_length=100)
    treatment=models.CharField(max_length=100)
    staff=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    outlet=models.CharField(max_length=100, default="room")

class Staff(models.Model):
    staff_name=models.CharField(max_length=100)
    expertise=models.CharField(max_length=100)
    nationality=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

class Appointments(models.Model):
    customer_n=models.CharField(max_length=100)
    customer_area=models.CharField(max_length=100)
    treatment=models.CharField(max_length=100)
    time=models.CharField(max_length=100,default="vi")
    staff_id=models.CharField(max_length=100,default="no")

class Rejected(models.Model):
    c_n=models.CharField(max_length=100)
    c_area=models.CharField(max_length=100)
    tment=models.CharField(max_length=100)
    time=models.CharField(max_length=100,default="vi")
    s_id=models.CharField(max_length=100,default="no")
