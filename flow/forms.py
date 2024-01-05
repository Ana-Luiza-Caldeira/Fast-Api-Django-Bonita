from django import forms
from .models import Flow, Notification

class FlowForm(forms.ModelForm):
    class Meta:
        model = Flow
        fields = ['module', 'organization', 'description', 'state']

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['flow', 'typeNotification', 'state', 'reprocessable', 'manageable']

class NotificationFormEdit(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['typeNotification', 'state', 'reprocessable', 'manageable']
