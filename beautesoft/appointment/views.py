from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from rest_framework.views import APIView
#from .serializer import *
from .models import *
from django.contrib import messages
from sales.views import *


#customer view their appointment requests
class Ur_app_rq(APIView):
    def get(self, request):
        conf = Appointments.objects.filter(customer_n=login.name)
        ur_rq = App_req.objects.filter(customer_n=login.name)
        return render(request,'ur_ap.html',{"ur_rq":ur_rq,"conf":conf})

#customer booking an appointment
class Book_app(APIView):
    def post(self, request):
        book.treatment=request.data.get('treatment')
        # print(book.treatment)
        return HttpResponseRedirect('book_app_load')
    def get(self, request):
        return render(request, 'book_app.html')#,{"staffs":staffs})
book = Book_app()

class Staff_load(APIView):
    def get(self, request):
        #print(book.treatment)
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
                    appoint = App_req.objects.create(staff=s.staff,
                                             customer_n=login.name,
                                             treatment=book.treatment,
                                             time=request.data.get('time'),
                                             outlet=request.data.get('outlet'))
                    print("sucessful")
                    return Response({"ok":"ok"})
                except Exception as e:
                    print(str(e))
                    return Response(str(e))
            else:
                print("already booked")
                return Response("data is already booked")
        else:
            print('already date booked')
            #messages.error(request, "date is already booked")
            return Response("data is already booked")
s = Staff_load()        
#management api
class Crm(APIView):
    def get(self, request):
        return render(request, 'crm.html')

#management adding their staff   
class Add_staff(APIView):
    def post(self, request):
        try:
            staff = Staff.objects.create(staff_name=request.data.get('staff_name'),
                            expertise=request.data.get('expertise'),
                            nationality=request.data.get('nationality'))
            return render(request, 'ad_ok.html')
        except Exception as e:
            return Response(str(e))

#staff login api
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

#staff profile api
class Staff_profile(APIView):
    def get(self, request):
        req = App_req.objects.filter(staff=obj_staff.n)
        con = Appointments.objects.filter(staff_id=obj_staff.n)
        return render(request, "staff_profile.html",{"req":req,"con":con})
    def post(self, request):
        k =request.data.get('name')
        if k:
            
            con = Appointments.objects.create(customer_n=request.data.get('name'),
                                                 customer_area=request.data.get('outlet'),
                                                 treatment=request.data.get('treatment'),
                                                 time=request.data.get('time'),
                                                 staff_id=obj_staff.n)
            App_req.objects.filter(staff=obj_staff.n,customer_n=request.data.get('name'),
                                     treatment=request.data.get('treatment'),outlet=request.data.get("outlet")).delete()
            return Response("sucess")
        else:
            nd=request.data.get('nd')
            td=request.data.get('td')
            od=request.data.get('od')
            ttd=request.data.get("ttd")
            print(nd)
            print(td)
            print(od)
            App_req.objects.filter(staff=obj_staff.n,customer_n=nd,
                                    treatment=td,
                                    outlet=od).delete()
            p=Rejected.objects.create(s_id=obj_staff.n,c_n=nd,tment=td,c_area=od,time=ttd)
            
            return Response("confirmed")
        # except Exception as e :
        #     print(str(e))
        #     return Response(str(e))




class Reject(APIView):
    def get(self, request):
        print(login.name)
        sentence = Rejected.objects.filter(c_n=login.name)


        return render(request, "reject.html",{"sentence":sentence})
