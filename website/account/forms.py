from django import forms
from .models import Account
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
    
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class ForgotForm(forms.Form):
    email = forms.EmailField()