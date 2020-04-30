from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30,required=False, help_text='Optional.')
    email= forms.EmailField(max_length=300, help_text='Required.Inform a valid Email')

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
