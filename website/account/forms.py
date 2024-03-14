from django import forms
from .models import Account, UserProfile
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
    )
    password = forms.CharField(
    label="Password",

    widget=forms.PasswordInput(
        attrs={'placeholder':'Enter Password', 'class':'form-control'}
    )
)

    class Meta:
        model = Account
        fields=('email','name','password','confirm_password') 
        
    def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")

            if password and confirm_password and password != confirm_password:
                 raise ValidationError("Passwords do not match")
            return cleaned_data
    
class UserForm(forms.ModelForm):
        class Meta:
             model = Account
             fields = ('name',)
    
class UserProfileForm(forms.ModelForm):
     class Meta:
          model = UserProfile
          fields = ('address_line_1','address_line_2', 'phone_number','city', 'state', 'country', 'profile_picture' )

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class ForgotForm(forms.Form):
    email = forms.EmailField()

class ResetForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    confirmpassword = forms.CharField(widget=forms.PasswordInput)


class OtpForm(forms.Form):
    otp = forms.IntegerField()