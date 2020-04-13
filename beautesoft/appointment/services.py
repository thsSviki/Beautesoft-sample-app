from .models import *
from . import views
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

def AppointmentReqCreation():
    appoint = App_req.objects.create(staff=views.s.staff,
                                    customer_n=views.s.customer_n,
                                    treatment=views.s.treatment,
                                    time=views.s.time,
                                    outlet=views.s.outlet)

def AddStaffCreation():
    user = User.objects.create_user(username=add.staff_name,
                                    email=add.email,
                                    password=add.password)
    token,_= Token.objects.get_or_create(user=user)
    staff = Staff.objects.create(staff_name=add.staff_name,
                                expertise=add.expertise,
                                nationality=add.nationality,
                                email=add.email,
                                password=add.password)

def AppointmentCreation():
    con = Appointments.objects.create(customer_n=views.pro.customer_n,
                                      customer_area=views.pro.customer_area,
                                      treatment=views.pro.treatment,
                                      time=views.pro.time,
                                      staff_id=views.pro.staff_id)
    App_req.objects.filter(staff=views.pro.staff_id,
                            customer_n=views.pro.customer_n,
                            treatment=views.pro.treatment,
                            outlet=views.pro.customer_area).delete()

def RejectedCreation():
    App_req.objects.filter(staff=views.pro.staff_id,
                            customer_n=views.pro.nd,
                            treatment=views.pro.td,
                            outlet=views.pro.od).delete()
    p=Rejected.objects.create(s_id=views.pro.staff_id,
                                c_n=views.pro.nd,
                                tment=views.pro.td,
                                c_area=views.pro.od,
                                time=views.pro.ttd)
