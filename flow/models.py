from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
 
class Flow(models.Model):
 
    process_id = models.CharField(max_length=50)
    module = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    state = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
 
    class Meta:       
        verbose_name='Flow'
        verbose_name_plural='Flows'
        unique_together = ('process_id', 'module', 'organization')
   
    def __str__(self):
        return f'{self.process_id} - {self.module} - {self.organization}'
 
 
class Notification(models.Model):
 
    flow = models.ForeignKey(Flow, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=50)
    typeNotification = models.CharField(max_length=50)
    state = models.BooleanField(default=True)
    reprocessable = models.BooleanField(default=False)
    manageable = models.BooleanField(default=False)
 
    class Meta:       
        verbose_name='Notification'
        verbose_name_plural='Notifications'
 
    def __str__(self):
        return f'{self.flow} - {self.transaction_id}'
 
 
class OriginConnection(models.Model):
 
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    typeOriginConnection = models.CharField(max_length=50)
    protocol = models.CharField(max_length=50)
    url = models.URLField()
    origin_id = models.CharField(max_length=50)

    class Meta:       
        verbose_name='Origin Connection'
        verbose_name_plural='Origin Connections'
 
    def __str__(self):
        return f'{self.notification} - {self.typeOriginConnection}'
   
 
class DestinyConnection(models.Model):
 
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    typeDestinyConnection = models.CharField(max_length=50)
    protocol = models.CharField(max_length=50)
    url = models.URLField()
    destiny_id = models.CharField(max_length=50)
#    ociiD_objectStorage =
#    ociiD_file =
   
    class Meta:       
        verbose_name='Destiny Connection'
        verbose_name_plural='Destiny Connections'

    def __str__(self):
        return f'{self.notification} - {self.typeDestinyConnection}'
 
 
class Data(models.Model):
 
    name = models.CharField(max_length=50)
 
    class Meta:       
        verbose_name='Data'
        verbose_name_plural='Datas'

    def __str__(self):
        return self.name
 
 
class Field(models.Model):

    data = models.ForeignKey(Data, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    typeField = models.CharField(max_length=50)
    searchable = models.BooleanField(default=False)
    editable = models.BooleanField(default=False)

    class Meta:       
        verbose_name='Field'
        verbose_name_plural='Fields'
 
    def __str__(self):
        return f'{self.name} - {self.typeField}'
   
 
class Rule(models.Model):
 
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    typeRules = models.CharField(max_length=50)
    description = models.TextField
    prompt = models.CharField(max_length=50)

    class Meta:       
        verbose_name='Rule'
        verbose_name_plural='Rules'
 
    def __str__(self):
        return f'{self.field} - {self.typeRules}'