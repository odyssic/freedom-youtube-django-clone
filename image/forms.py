from django import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(label='Password', max_length=20)

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(label='Password', max_length=20)
    email = forms.CharField(label='Email', max_length=20)

class NewImageForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='Description', max_length=1000)
    image = forms.FileField(label="Image")

    #Add to a form containing a FileField and change the field names accordingly.

    def clean_content(self):
        content = self.cleaned_data['image']
        content_type = content.content_type.split('/')[0]
        
        if content_type in settings.CONTENT_TYPES:
            if content._size > settings.MAX_UPLOAD_SIZE:
                raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content._size)))
        else:
            raise forms.ValidationError(_('File type is not supported'))
        return content

class CommentForm(forms.Form):
    text = forms.CharField(label='Comment', max_length=500)
    image = forms.IntegerField(widget=forms.HiddenInput(), initial=1)

