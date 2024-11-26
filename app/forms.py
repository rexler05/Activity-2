from django import forms
from django.forms.widgets import ClearableFileInput
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'animal', 'breed', 'age', 'description', 'post_image']
        widgets = {
            'post_image': ClearableFileInput(attrs={'class': 'form-control'}),
        }


