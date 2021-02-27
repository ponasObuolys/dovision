from django import forms
from django.forms.widgets import DateInput

from doVision.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'due_date']
        widgets = {
            'due_date': DateInput(attrs={'type': 'date'}),
        }


class DateInput(forms.DateInput):
    input_type = 'date'
