from django.db import models
from django import forms
from django.forms import ModelForm

from .models import Task


class TaskForm(ModelForm):
    content = forms.CharField(label='Content',
                              max_length=200,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Task
        fields = ['content']
