from django.db import models
from .models import MyImage
from django.forms import fields
from django import forms
from .models import AES_Image


class AESImageForm(forms.ModelForm):
    class Meta:
        model = AES_Image
        fields = "__all__"
