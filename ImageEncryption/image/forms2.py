from django.db import models
from .models import MyImage
from django.forms import fields
from django import forms
from .models import AES_Image


class AESImageForm(forms.ModelForm):
    class Meta:
        model = AES_Image
        fields = "__all__"
        widgets={
            'key': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter a secret key of image'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
