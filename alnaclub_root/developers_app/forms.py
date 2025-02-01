from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'roi', 'funds_needed', 'estimated_completion_time', 'work_progress']
        widgets = {
            'work_progress': forms.Select(choices=Project.PROGRESS_CHOICES),
        }
