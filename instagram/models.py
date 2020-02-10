from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User




class Profile(models.Model):
   profile_photo = models.ImageField(blank=True) 
   bio = models.TextField()