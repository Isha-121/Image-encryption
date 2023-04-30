from django.db import models
from .models import MyImage
from django.forms import fields
from django import forms
from .models import AES_Image


class UploadedImage(forms.ModelForm):
    class Meta:
        # specify the model to be used to create form
        model = MyImage
        # include all the fileds of the model
        fields = "__all__"
        
        widgets={
            'caption': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Caption of image'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
