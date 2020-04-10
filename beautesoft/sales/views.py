from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse,HttpResponseRedirect
from rest_framework.views import APIView
from .serializer import *
from .models import *
import stripe 
from django.conf import settings 



stripe.api_key = settings.STRIPE_SECRET_KEY

class Customer(APIView):
    def get(self, request):
        #print('1')
        return render(request,'register.html')
    def post(self, request):
        se = UserSerializer(data=request.data)
        if se.is_valid(raise_exception=True):
            user_exist = Custom.objects.filter(email=request.data.get('email')).exists()
            name_exist= Custom.objects.filter(name=request.data.get('name')).exists()
            if not user_exist:
                if not name_exist:
                    try:
                #print("2")
                        customer = Custom.objects.create(
                            name=request.data.get('name'),
                            email=request.data.get('email'),
                            password=request.data.get('password'))
                #print('viki')
                        return HttpResponseRedirect('log')
                    except Exception as e:
                        return Response({"Response": str(e)})
                else:
                    return Response("user name is already taken")
            else:
                return Response("email id is already exist")


class Login(APIView):
    def get(self, request):
        return render(request, "login.html")
    def post(self, request):
        user_exist = Custom.objects.filter(email=request.data.get('email')).exists()
        name = Custom.objects.get(email=request.data.get('email'))
        print(name)
        #for i in name:
            #print(i.name)
        #login.name=name.name
        print(name.name)
        login.name=name.name
        print(login.name)
        ps = Custom.objects.filter(
        email=request.data.get('email'),
        password=request.data.get('password'))
        if  user_exist:
            if  ps:
                obj.n=request.data.get("email")
                return HttpResponseRedirect('home')
            else:
                return Response("plz verify your email or password")
        else:
            return  Response("Email is not registered")

obj = Login()
login = Login()

class Catalog(APIView):
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
            k = Purchase.objects.create(
                        product=request.data.get('product'),price=request.data.get('price'),purchaser=obj.n)
            print("4")
            return Response("ok")
        except Exception as e:
            return Response(str(e))
            
cat = Catalog()

#class Cart(APIView):
 #   def get(self, request):
  #      items = Purchase.objects.filter(purchaser=obj.n)

   #     return render(request,'cart.html',{"items":items})
   # def post(self, request):
    #    try:
     #       k = Purchase.objects.create(
      #                  product=request.data.get('product'),price=request.data.get('price'),purchaser=obj.n)
       #     print("4")
        #    return Response('ok')
        #except Exception as e:
         #   return HttpResponse(str(e))
class Pay(APIView):
    #template_name = 'paygate.html'

    def get(self,request,**kwargs): # new
        context = {}#super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        tot = {"tot":cat.total}
        tot.update(context) 
        return render(request,'paygate.html',tot)
   

class Charge(APIView): 
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
        
       
