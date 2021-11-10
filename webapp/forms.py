from django import forms
from .models import detail

class detailform(forms.ModelForm):
    class Meta:
        model=detail
        fields=('time','frame')

