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


class AESImageForm(forms.ModelForm):
    class Meta:
        model = AES_Image
        fields = "__all__"
