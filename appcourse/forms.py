from django import forms
from appcourse.models import centermodel,studentregistration
import time



class centerform(forms.ModelForm):
    date = forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    time = forms.CharField(max_length=25)
    class Meta:
        model = centermodel
        fields="__all__"

class studentform(forms.ModelForm):
    class Meta:
        model = studentregistration
        fields="__all__"




