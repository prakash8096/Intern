from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile



class Forms(UserCreationForm):
    
    email=forms.EmailField()
    # lastname=forms.CharField(max_length=30)
    # password1=forms.PasswordInput()


    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UserModify(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']