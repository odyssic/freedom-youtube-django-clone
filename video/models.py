from django.db import models
from .validators import validate_file_extension

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    path = models.CharField(max_length=60)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Comment(models.Model):
    body = models.TextField(max_length=300)
    datetime = models.DateTimeField(blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

#user
#favorites
#votes
