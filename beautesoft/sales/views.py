from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse,HttpResponseRedirect
from rest_framework.views import APIView
from .serializer import *
from .models import *
import stripe 
from django.conf import settings 
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .services import *



stripe.api_key = settings.STRIPE_SECRET_KEY

class Customer(APIView):
    def get(self, request):
        
        return render(request,'register.html')
    def post(self, request):
        se = UserSerializer(data=request.data)
        if se.is_valid(raise_exception=True):
            user_exist = Custom.objects.filter(email=request.data.get('email')).exists()
            name_exist= Custom.objects.filter(name=request.data.get('name')).exists()
            obj_c.name=request.data.get('name')
            obj_c.email=request.data.get('email')
            obj_c.password=request.data.get('password')
            if not user_exist:
                if not name_exist:
                    try:
                        customer()
                        TokenCreation()
                        
                        return HttpResponseRedirect('log')
                    except Exception as e:
                        return Response({"Response": str(e)})
                else:
                    return Response("user name is already taken")
            else:
                return Response("email id is already exist")
obj_c = Customer()

class Login(APIView):
    def get(self, request):
        return render(request, "login.html")
    def post(self, request):
        user_exist = Custom.objects.filter(email=request.data.get('email')).exists()
        
        ps = Custom.objects.filter(
        email=request.data.get('email'),
        password=request.data.get('password'))
        if  user_exist:
            if  ps:
                name = Custom.objects.get(email=request.data.get('email'))
                login.name=name.name
                obj.n=request.data.get("email")
                return HttpResponseRedirect('home')
            else:
                return Response("plz verify your email or password")
        else:
            return  Response("Email is not registered")

obj = Login()
login = Login()

class Catalog(APIView):
    
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        try:
            pro = Product.objects.all()
            items = Purchase.objects.filter(purchaser=obj.n)
            total = 0
            for i in items:
                total += i.price                    
            cat.total = total
            return render(request,"home.html",{"pro":pro,"items":items,"total":total})
       

        except Exception as e:
            return Response({"response":str(e)})
    def post(self, request):
        try:
            pur = Purchase.objects.filter(purchaser=obj.n)
            cat.product = request.data.get('product')
            cat.price = request.data.get('price')
            cat.purchaser = purchaser=obj.n
            PurchaseCreation()
            return Response("ok")
        except Exception as e:
            return Response(str(e))
            
cat = Catalog()

class Pay(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def get(self,request,**kwargs): 
        context = {}
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        tot = {"tot":cat.total}
        tot.update(context) 
        return render(request,'paygate.html',tot)
   

class Charge(APIView): 
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        charge = stripe.Charge.create(
                amount = int(cat.total),
                currency='INR',
                description='A Django charge',
                source=request.POST['stripeToken']
            )       
        Purchase.objects.filter(purchaser=obj.n).delete()
        return render(request, 'charge.html')

    def get(self,request):
        return render(request, 'charge.html')
        
       
