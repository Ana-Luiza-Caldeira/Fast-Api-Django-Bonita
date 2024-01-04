from django import forms
from .models import Flow, Notification

class FlowForm(forms.ModelForm):
    class Meta:
        model = Flow
        fields = ['process_id', 'module', 'organization', 'description', 'state']

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['flow', 'transaction_id', 'typeNotification', 'state', 'reprocessable', 'manageable']
