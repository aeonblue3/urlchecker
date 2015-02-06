from django.db import models
from django import forms

# Create your models here.
class UrlForm(forms.Form):
  url = forms.URLField(
    label='',
    error_messages = {'required': 'Please enter a url.', 'invalid': 'Please enter a valid url.'},
    widget=forms.URLInput(attrs={'placeholder': 'Url', 'class': 'form-control'})
  )
