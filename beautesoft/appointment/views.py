from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .models import *
from django.contrib import messages
from sales.views import *
from .services import *



class Ur_app_rq(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        conf = Appointments.objects.filter(customer_n=login.name)
        ur_rq = App_req.objects.filter(customer_n=login.name)
        return render(request,'ur_ap.html',{"ur_rq":ur_rq,"conf":conf})


class Book_app(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self, request):
        book.treatment=request.data.get('treatment')
        
        return HttpResponseRedirect('book_app_load')
    def get(self, request):
        return render(request, 'book_app.html')
book = Book_app()

class Staff_load(APIView):
    def get(self, request):
        
        staf = Staff.objects.filter(expertise=book.treatment)

        return render(request, 'book_app_load.html',{"staf":staf,"treatment":book.treatment})
    def post(self, request):
        if request.data.get("test"):
            s.staff = request.data.get('staff')
        free = App_req.objects.filter(staff=s.staff,time=request.data.get('time')).exists()
        free1 = Appointments.objects.filter(staff_id=s.staff,time=request.data.get('time')).exists()
        if not free:
            if not free1:
                try:
                    s.customer_n=login.name 
                    s.treatment = book.treatment
                    s.time = request.data.get('time')
                    s.outlet = request.data.get('outlet') 
                    AppointmentReqCreation()
                    
                    return Response({"ok":"ok"})
                except Exception as e:
                    
                    return Response(str(e))
            else:
                
                return Response("data is already booked")
        else:
            
            return Response("data is already booked")
s = Staff_load()      

class Crm(APIView):
    def get(self, request):
        return render(request, 'crm.html')

  
class Add_staff(APIView):
    def get(self, request):
        return render(request, "add_staff.html")
    def post(self, request):
        add.staff_name=request.data.get('staff_name')
        add.expertise=request.data.get('expertise')
        add.nationality=request.data.get('nationality')
        add.email=request.data.get('email')
        add.password=request.data.get('password')
        try:
            AddStaffCreation()
            return render(request, 'ad_ok.html')
        except Exception as e:
            return Response(str(e))

add = Add_staff()
class Staff_login(APIView):
    def get(self, request):
        return render(request,"staff_login.html")
    def post(self, request):
        if request.data.get("email")=="admin@g.com" and request.data.get("password")=="admin":
            admin = Appointments.objects.all()
            return render(request,"admin.html",{"admin":admin})
        user_exist = Staff.objects.filter(email=request.data.get('email')).exists()
        ps = Staff.objects.filter(
            email=request.data.get('email'),
            password=request.data.get('password'))
        if user_exist:
            if  ps:
                staff = Staff.objects.get(email=request.data.get('email'))
                obj_staff.n=staff.staff_name
                return HttpResponseRedirect('staff_profile')
            else:
                return Response("plz check ur email or password")
        else:
            return Response("email is not valid")
obj_staff = Staff_login()


class Staff_profile(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        req = App_req.objects.filter(staff=obj_staff.n)
        con = Appointments.objects.filter(staff_id=obj_staff.n)
        return render(request, "staff_profile.html",{"req":req,"con":con})
    def post(self, request):
        k =request.data.get('name')
        if k:
            pro.customer_n=request.data.get('name'),
            pro.customer_area=request.data.get('outlet'),
            pro.treatment=request.data.get('treatment'),
            pro.time=request.data.get('time'),
            pro.staff_id=obj_staff.n
            AppointmentCreation()
            return Response("success")
        else:
            pro.nd=request.data.get('nd')
            pro.td=request.data.get('td')
            pro.od=request.data.get('od')
            pro.ttd=request.data.get("ttd")
            RejectedCreation()            
            return Response("confirmed")
       
pro = Staff_profile()



class Reject(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        
        sentence = Rejected.objects.filter(c_n=login.name)


        return render(request, "reject.html",{"sentence":sentence})