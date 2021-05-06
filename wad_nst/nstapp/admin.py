from django.contrib import admin
from .models import Profile


# Register your models here so that we can see model
# when we login to admin page.

admin.site.register(Profile)