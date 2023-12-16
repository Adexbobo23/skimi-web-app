from django import forms
from .models import StatusUpdate

class StatusUpdateForm(forms.ModelForm):
    class Meta:
        model = StatusUpdate
        fields = ['image']
