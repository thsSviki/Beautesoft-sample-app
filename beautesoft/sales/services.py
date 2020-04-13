from .models import *
from . import views
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

def customer():
    customer = Custom.objects.create(
                            name=views.obj_c.name,
                            email=views.obj_c.email,
                            password=views.obj_c.password)
    return 1

def TokenCreation():
    user = User.objects.create_user(username=views.obj_c.name,
                                    email=views.obj_c.email,
                                    password=views.obj_c.password)
    token,_= Token.objects.get_or_create(user=user)

def PurchaseCreation():
    k = Purchase.objects.create(
                        product=views.cat.product,
                        price=views.cat.product,
                        purchaser=views.obj.n)