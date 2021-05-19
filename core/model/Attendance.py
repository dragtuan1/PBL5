from django.db import models

class Attendance(models.Model):
    #id = models.IntegerField(primary_key=True, max_length=255)
    timeattend = models.TextField(default='')
    total = models.TextField(default='')
    absent = models.TextField(default='')
    schedule = models.ForeignKey('core.Schedule', on_delete=models.CASCADE, default='')
    