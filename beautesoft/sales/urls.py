from django.urls import path,include
from .views import *

urlpatterns = [
    path('',Customer.as_view()),
    path('log',Login.as_view()),
    path('home',Catalog.as_view()),
    path('paygate',Pay.as_view()),
    path('charge',Charge.as_view()),

]
