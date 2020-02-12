from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




class Profile(models.Model):
    profile_photo = models.ImageField(blank=True,default='images/insta2.jpeg') 
    bio = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    def create_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()

class Image(models.Model):
    image_name = models.CharField(max_length =30)
    image_photo = ImageField(blank=True, manual_crop="")
    image_caption = models.TextField()
    image_profile = models.ForeignKey(Profile,on_delete=models.CASCADE )
    image_likes = models.IntegerField(default = 0,null=True)
    image_comments = models.TextField(default=0, blank = True) 
        
    def __str__(self):
        return self.image_name


    class Meta:
        ordering = ['image_name']

    @classmethod
    def get_all(cls):
        imgs = Image.objects.all()
        return imgs

    def save_image(self):
        """
        Save a new image to the database    
        """
        self.save()
        
    def delete_image(self):
        """
        function to delete an image from the db
        """
        self.delete()

    def update_image(self):
      """
      function to update the caption of an image
      """
      self.image_caption.update() 

    @classmethod
    def search_by_profile(cls,search_term):
        image = cls.objects.filter(title__icontains=search_term)
        return image