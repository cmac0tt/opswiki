from django.db import models
from django import forms

class Page(models.Model):
    name = models.CharField(max_length=25, primary_key=True)
    content = models.TextField(blank=True)

class UploadFileForm(forms.Form):
        title = forms.CharField(max_length=50)
        file  = forms.FileField()
