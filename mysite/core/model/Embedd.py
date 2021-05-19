from django.db import models
#from core.model import Schedule
class Embedd(models.Model):
    #idschedule = models.ForeignKey('core.Schedule', unique = True, on_delete=models.CASCADE, default='')
    #id = models.CharField(primary_key=True, max_length=255)
    dess = models.CharField(max_length=100)
    embedd = models.BinaryField(max_length=255)