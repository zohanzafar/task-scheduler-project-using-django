from django import forms
from .models import Project, Task

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-lg w-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter a project title', 
            }),
            'description': forms.Textarea(attrs={
                'class': 'border border-gray-300 rounded-lg w-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'rows': 6,  
                'style': 'max-height: 10em; overflow-y: auto;',
                'placeholder': 'Enter a project description', 
            }),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-lg w-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter a task title', 
            }),
            'description': forms.Textarea(attrs={
                'class': 'border border-gray-300 rounded-lg w-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'rows': 6,  
                'style': 'max-height: 10em; overflow-y: auto;',
                'placeholder': 'Enter a task description', 
            }),
            'status': forms.Select(attrs={
                'class': 'border border-gray-300 rounded-lg w-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'due_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'border border-gray-300 rounded-lg w-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
        }
