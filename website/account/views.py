from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm,LoginForm,OtpForm,ForgotForm,ResetForm
from django.conf import settings
from django.core.mail import send_mail
from .models import Account, UserProfile
import pyotp
from functools import wraps
from .forms import UserForm,UserProfileForm

def logout_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return view_func(request, *args, **kwargs)

    return _wrapped_view

@logout_required
def loginn(request):
    if request.method == 'POST': 
        form=LoginForm(request.POST)
        try:
            if form.is_valid():
                email = form.cleaned_data.get('email')
                
                password = form.cleaned_data.get('password')
                
                user = authenticate(email=email, password=password)
                
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid email or password.')
            else:
                messages.error(request, 'Form is not valid.') 

        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
        return redirect('login')
    else:
        form = LoginForm() 
    return render(request, 'login.html', {'form': form})

#@logout_required
def signup(request):
    if request.method == 'POST': 
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('name')
            raw_pass = form.cleaned_data.get('password')
            user = Account.objects.create_user(email=email,password=raw_pass,name=name)
            user.save()

            subject='Fashion Wolrd OTP Verification'
            totp = pyotp.TOTP(pyotp.random_base32())
            otp = totp.now()
            request.session['generated_otp'] = otp 
            message=f'Your registeration otp is {otp} '
            recipient=user.email
            print(otp, recipient)
            print(send_mail,settings.EMAIL_HOST_USER, 'mmmmmmmmmmmmmmmmmmm' )
            send_mail(subject,message,settings.EMAIL_HOST_USER,[recipient],fail_silently=False)
            # return redirect('login')
            return redirect('otp',user.id)
        else:
            messages.error(request, "Please Correct Below Errors")
                    
    else:
        form = RegistrationForm()
        
    return render(request,'signup.html',{'registration_form':form})

def Verify_otp(request, id):
    user = Account.objects.get(id=id)
    otp = request.session.get('generated_otp')
    print(type(otp),'sdefsdf')
    if request.method == "POST":
        form = OtpForm(request.POST)
        if form.is_valid():
            otp_input = form.cleaned_data.get('otp')
            print(type(otp_input), "sdflkbfk")
            print(otp == otp_input)
            if otp == str(otp_input):
                user.is_active = True  
                user.save()
                messages.success(request, 'Your Account is Activated, now you can Login.')
                return redirect('login')  
            else:
                messages.error(request, 'Invalid otp, Please try again.')
                return redirect('otp', id=id) 
    else:
        form = OtpForm()
        return render(request, 'user/otpRegistraion.html',{'form':form})
                      
def logout_user(request):
        logout(request)
        return redirect('home')

def forgot_password(request):
    if request.method == 'POST':
        form = ForgotForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                user = Account.objects.get(email=email)
                print(user.id)
                messages.success(request, 'Password reset email sent successfully.')
                return redirect('resetpassword', id=user.id)
            except Account.DoesNotExist:
                messages.error(request, 'Account with this email does not exist.')
    else:
        form = ForgotForm()
    return render(request, 'forgetPassword.html', {'form': form})

def reset_password(request, id):
    user = Account.objects.get(id=id)
    print('hai', user)
    if request.method == 'POST':
        form = ResetForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            confirmpassword = form.cleaned_data.get('confirmpassword')
            if password and confirmpassword and password != confirmpassword:
                raise form.ValidationError('password is not match')
            else:
                user.set_password(password)
                user.save()
                return redirect('login')
    else:
        form =ResetForm()
    return render(request, 'resetpassword.html',{'form':form})

def userProfiles(request):
    userprofile = Account.objects.get(id=request.user.id)
    print(userprofile.name)
    #userprofile=get_object_or_404(UserProfile, user=request.user) 
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
       
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your Profile has been updated.')
            return redirect('profiles')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=userprofile)

    context = {
        'user_form' : user_form,
        'profile_form' : profile_form,
    }
    return render(request,'user/profile.html', context)


def home(request):
    return render(request,'user/home.html') 
def service(request):
    return render(request,'user/service.html')
def contact(request):
    return render(request,'user/contact.html')

def sample(request):
    return render(request,'user/sample.html')