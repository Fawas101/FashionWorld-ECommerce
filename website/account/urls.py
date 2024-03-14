from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginn, name="login"),
    path('logout/',views.logout_user, name="logout"),
    path('signup/',views.signup, name="signup"),
    path('',views.home, name="home"),
    path('forgetPassword/',views.forgot_password, name="forgetPassword"),
    path('services/',views.service, name="services"),
    path('contact/',views.contact, name="contact"),
    path('otp/<int:id>/',views.Verify_otp, name='otp'),
    path('profile/',views.userProfiles, name="profiles"),
    path('s/',views.sample, name="s"),
    path('resetpassword/<int:id>/',views.reset_password, name="resetpassword"),
    
]
