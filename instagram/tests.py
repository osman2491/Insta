from django.test import TestCase
from .models import Image, Profile
from django.contrib.auth.models import User

# Create your tests here.
class ImageTestClass(TestCase):
   # Setup Method
   def setUp(self):
      self.profile=Profile(id = 1)
      self.image_one=Image(image_name='moana',image_caption='By the seashore',image_comments= 'Quality image')

    # Testing Instance
   def test_instance(self):
      self.assertTrue(isinstance(self.image_one,Image))


   # Testing Save Method
   def test_save_method(self):
      self.image_one.save_image()
      imgs = Image.objects.all()
      self.assertTrue(len(imgs) > 0)