from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegistrationForm,LoginForm,ForgotForm
from django.conf import settings
from django.core.mail import send_mail
from .models import Account


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
                    return redirect('/home')
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

def signup(request):
    if request.method == 'POST': 
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('name')
            raw_pass = form.cleaned_data.get('password')
            user = Account.objects.create_user(email=email,password=raw_pass,name=name)
            user.save()
            
            return redirect('login')
        else:
            messages.error(request, "Please Correct Below Errors")
            
    else:
        form = RegistrationForm()
        
    return render(request,'signup.html',{'registration_form':form})

def home(request):
    return render(request,'user/home.html') 
def service(request):
    return render(request,'user/service.html')
def contact(request):
    return render(request,'user/contact.html')
