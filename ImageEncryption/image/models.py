from django.db import models


# Create your models here.
class MyImage(models.Model):
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.caption


class AES_Image(models.Model):
    key = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.caption
