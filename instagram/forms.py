from django import forms
from .models import Image
from pyuploadcare.dj.forms import ImageField

class PostForm(forms.ModelForm):

    class Meta:
        model = Image
        fields=('image_name','image_caption','image_photo')