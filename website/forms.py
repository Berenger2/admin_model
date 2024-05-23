from django import forms
from .models import *

class AddModelForm(forms.ModelForm):
    experience = forms.ModelChoiceField(queryset=Experience.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Experience'}))
    libelle = forms.CharField(label='Name', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Libelle'}))
    description = forms.CharField(label='Description',required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}))
    path = forms.FileField(label='Model',required=False, widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'File', 'accept': '.h5,.pkl'}))


    class Meta:
        model = Model
        fields = ['libelle', 'description', 'path', 'experience']
        # exclude = ['slug', 'score', 'path', 'state', 'status', 'created_at']
        
        



class AddExperinceForm(forms.ModelForm):
    libelle = forms.CharField(label='Name', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Libelle'}))
    description = forms.CharField(label='Description',required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}))
    class Meta:
        model = Experience
        fields = ['libelle', 'description']
        # exclude = ['slug', 'score', 'path', 'state', 'status', 'created_at']
