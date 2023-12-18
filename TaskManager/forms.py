from django import forms
from .models import *
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User


class CreateTaskForm(forms.ModelForm):
    TASK_TYPE_CHOICES = [
        ('property_networks', 'Property Networks'),
        ('list', 'List' ),
    ]
    task_type = forms.ChoiceField(choices=TASK_TYPE_CHOICES, initial='open', widget=forms.Select(attrs={'class': 'form-select'}))
    class Meta:
        model = TasksList
        fields = ['task_name', 'task_description', 'deadline', 'task_type','task_content']
        labels = {
            'task_name': "Nombre",
            'task_description': 'Descripcion',
            'deadline' : 'Fecha de finalizacion',
            'task_content': 'Contenido',
            'task_type': 'type',
        }
        widgets = {
            'deadline': forms.TextInput(attrs={'type': 'datetime-local'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['task_content'].initial = 'contenido'
        self.fields['task_description'].initial = 'Nueva Tarea'        

# class TasksListForm(forms.ModelForm):
#     class Meta:
#         model = TasksList
#         fields = ['task_name', 'task_description', 'task_content', 'deadline', 'open']
#         widgets = {
#             'deadline': forms.TextInput(attrs={'type': 'datetime-local'}),
#         }

# class CreateCommentForm(forms.ModelForm):
#     class Meta:
#         model = TasksListRows
#         fields = ['task_comment', 'state', 'date', 'comment']
#         labels = {
#             'task_comment': "Nombre",
#             'state': 'Descripcion',
#             'date' : 'Fecha de finalizacion',
#             'comment': 'comentario',
#         }
#         widgets = {
#             'date': forms.TextInput(attrs={'type': 'datetime-local'}),
#         }

# class CommentCreationForm(forms.Form):

#     comment = forms.CharField(widget=forms.Textarea)
#     state = forms.BooleanField(widget=forms.HiddenInput(), initial=True)
#     task_comment = forms.ModelChoiceField(widget=forms.HiddenInput(),queryset=TasksList.objects.all())

