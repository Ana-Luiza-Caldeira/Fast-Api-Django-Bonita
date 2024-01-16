from django import forms
from .models import Flow, Notification

class FlowForm(forms.ModelForm):
    class Meta:
        model = Flow
        fields = ['process_id', 'module', 'organization', 'description', 'state']

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['transaction_id','flow', 'typeNotification', 'state', 'reprocessable', 'manageable']

class FlowFormEdit(forms.ModelForm):
    class Meta:
        model = Flow
        fields = ['module', 'organization', 'description', 'state']

class NotificationFormEdit(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['typeNotification', 'state', 'reprocessable', 'manageable']
