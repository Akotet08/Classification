from distutils.command.upload import upload
from enum import auto
from django.db import models
from pkg_resources import require

# Create your models here.
class Image(models.Model):
    upload_image = models.ImageField(upload_to='media/%Y/%m/%d/')
    upload_date = models.DateTimeField(auto_now_add=True)