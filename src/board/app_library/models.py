from django.db import models



# Create your models here:
class Publisher(models.Model):

    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=50)
    is_active = models.BooleanField()
    
    
class Author(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    biography = models.TextField()