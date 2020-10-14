from django.db import models
from .validators import validate_file_extension

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=100)
    path = models.CharField(max_length=100, validators=[validate_file_extension])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False) #todo: auto_now=True
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = creat_shortcode(self)

    def __str__(self):
        return str(self.path)

    def __unicode__(self):
        return str(self.url)

    def get_tiny_url(self):
        url_path = reverse("scode", kwargs={'shortcode': self.shortcode})
        return "http://tiny.com" + url_path

class Comment(models.Model):
    text = models.TextField(max_length=300)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

