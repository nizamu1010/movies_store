from dataclasses import field
from django import forms
from .models import movie

class mv_form(forms.ModelForm):
    class Meta:
        model = movie
        fields = ['name', 'desc', 'year', 'img']
