from django import forms
from django.forms import ModelForm

from .models import TodoList


class TodoListForm(forms.ModelForm):

    class Meta:
        model = TodoList
        fields = '__all__'
