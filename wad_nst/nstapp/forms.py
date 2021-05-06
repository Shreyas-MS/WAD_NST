from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Feedback
from django.forms import ModelForm

"""
    Building the new form UserRegistrationFOrm from the 
    UserCreationForm for the model user so that we can add
    an extra field email. 

"""

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class FeedbackForm(ModelForm):
    class Meta :
        model = Feedback
        fields = ['email','title','feedback']