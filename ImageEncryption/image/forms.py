from django.db import models
from .models import MyImage
from django.forms import fields
from django import forms


class UploadedImage(forms.ModelForm):
    class Meta:
        # specify the model to be used to create form
        model = MyImage
        # include all the fileds of the model
        fields = "__all__"
