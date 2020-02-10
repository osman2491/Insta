from django import forms
from .models import Image,Profile
from pyuploadcare.dj.forms import ImageField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):

    class Meta:
        model = Image
        fields=('image_name','image_caption','image_photo')
class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_photo']