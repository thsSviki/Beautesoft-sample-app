from .views import *
from django.urls import path,include

urlpatterns = [
    path('book_app',Book_app.as_view()),
    path('book_app_load',Staff_load.as_view()),
    path('ur_app',Ur_app_rq.as_view()),
    path('staff_log',Staff_login.as_view()),
    path('staff_profile',Staff_profile.as_view()),
    path('rejected',Reject.as_view())

]