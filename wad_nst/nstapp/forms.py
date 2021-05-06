from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Feedback,Profile
from django.forms import ModelForm


class UserRegistrationForm(UserCreationForm):
    """
    Building the new form UserRegistrationFOrm from the 
    UserCreationForm for the model user so that we can add
    an extra field email. 

    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class FeedbackForm(ModelForm):
    class Meta :
        model = Feedback
        fields = ['email','title','feedback']

""" 
    UserUpdateForm and ProfileUpdateForm these two forms were created 
    serve the purpose of profile update form.
    
"""

class UserUpdateForm(ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']