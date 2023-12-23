from django import forms 
from .models import User 

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ["username", "password"]
        widgets = {"password": forms.PasswordInput()}
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    
    