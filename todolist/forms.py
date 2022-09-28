from django import forms
from . import models

class CreateTaskForm(forms.ModelForm) :
    class Meta:
        model = models.Task
        fields = ['title', 'description']
        title = forms.CharField(max_length=255)
        description = forms.TextInput()