from datetime import timezone
from django.db import models

# Create your models here.

#MODEL SUPER USUARIO 
class superUser(models.Model):
    correoUser = models.CharField(primary_key=True, max_length= 50, null=False)
    nombreUser = models.CharField(max_length=100, null=False)
    contraUser = models.CharField(max_length= 15, null=False)