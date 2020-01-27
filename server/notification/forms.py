from django import forms
from .models import notification
class notificationForm(forms.Form):
    name = forms.CharField()
    title = forms.CharField()
    date_added = forms.DateTimeField()
    status = forms.IntegerField()
