from django.db import models
from .validators import validate_file_extension
from django.conf import settings

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=100)
    path = models.CharField(max_length=100, validators=[validate_file_extension])
    image = models.FileField(upload_to='images/', null=False)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False) 
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    # def __str__(self):
    #     return str(self.path)


class Comment(models.Model):
    text = models.TextField(max_length=300)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

