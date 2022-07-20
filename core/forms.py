from django.forms import ModelForm
from core.models import RegisteredAssets
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisteredAssetsForm(ModelForm):
    class Meta:
        model = RegisteredAssets
        fields = '__all__'
        exclude= ['investor', 'price']

class UserCreation(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

