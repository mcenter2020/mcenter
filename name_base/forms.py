from django import forms
from .models import Name_list
from django.forms import ModelForm
class PostForm(forms.ModelForm):

    class Meta:
        model = Name_list
        fields = ['comandname', 'capitan', 'city','phone', 'email', 'promotion', 'rebuke', 'image', 'slug', 'mark', 'mark2', 'mark3', 'mark4', 'mark5', 'mark6', 'mark7', 'mark8', 'mark9', 'mark10']


