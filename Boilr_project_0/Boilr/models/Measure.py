from django.db import models

class Measure(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.FloatField()
    unit = models.CharField(max_length=16)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE)
