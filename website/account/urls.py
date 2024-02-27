from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginn, name="login"),
    path('',views.signup, name="signup"),
    path('home/',views.home, name="home"),
    path('services/',views.service, name="services"),
    path('contact/',views.contact, name="contact"),
   
]
