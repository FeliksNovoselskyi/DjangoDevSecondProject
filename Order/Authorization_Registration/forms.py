from django import forms
from .models import Users

class RegForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['login', 'password', 'email', 'phone']
