from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from flow.models import Flow
 
 
class Role(models.Model):

    name = models.CharField(max_length=50, null=True)
    userRole = models.ManyToManyField(User, related_name='roles')

    class Meta:       
        verbose_name='Role'
        verbose_name_plural='Roles'

    def __str__(self):
        return self.name
 
class Authorization(models.Model):
    
    flowAuth = models.ForeignKey(Flow, on_delete=models.CASCADE, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    userAuthorization = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    class Meta:       
        verbose_name='Autorization'
        verbose_name_plural='Autorizations'
