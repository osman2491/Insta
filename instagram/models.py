from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User




class Profile(models.Model):
   profile_photo = models.ImageField(blank=True) 
   bio = models.TextField()

class Image(models.Model):
    image_name = models.CharField(max_length =30)
    image_photo = ImageField(blank=True, manual_crop="")
    image_caption = models.TextField()
    image_profile = models.ForeignKey(Profile,on_delete=models.CASCADE, default = 1)
    image_likes = models.IntegerField(default = 0,null=True)
    image_comments = models.TextField(blank = True) 
        
    def __str__(self):
        return self.image_name