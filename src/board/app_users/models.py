from django.db import models

from django.contrib.auth.models import User

#from django.contrib.auth.models import AbstractUser



# Create your models here:
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=36, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)