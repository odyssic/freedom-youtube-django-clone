from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(label='Password', max_length=20)

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(label='Password', max_length=20)
    email = forms.CharField(label='Email', max_length=20)

class NewImageForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    file = forms.ImageField()

class CommentForm(forms.Form):
    text = forms.CharField(label='Comment', max_length=500)
    image = forms.IntegerField(widget=forms.HiddenInput(), initial=1) 