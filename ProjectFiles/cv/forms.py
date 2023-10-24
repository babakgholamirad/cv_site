from django import forms
from django_select2.forms import ModelSelect2MultipleWidget

from .models import Project


class MembersWidget(ModelSelect2MultipleWidget):
    search_fields = [
        "first_name__icontains"
    ]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'client',
            'members',
            'description',
            'status',
            'progress',
            'start_date']
        widgets = {
            "members": MembersWidget
        }
