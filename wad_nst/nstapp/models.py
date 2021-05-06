from django.db import models
from PIL import Image
from django.contrib.auth.models import User

"""
    Creating a new model name Profile for our profile 
    page that is having Foreign key constraint with User 
    model. And other image field for profile pics that 
    will stored in profile_pics subolder inside media if they 
    upload or else default.jpg pic. 

"""

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'