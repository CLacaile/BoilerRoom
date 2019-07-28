from django.db import models

class Room(models.Models):
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    surface = models.FloatField()

class Sensor(models.Models):
    name = models.CharField(max_length=32)
    room = models.ForeignKey('Room', on_delete=models.SET_NULL)

class Measure(models.Models):
    value = models.FloatField()
    unit = models.CharField(max_length=16)
    time = models.DataTimeField(auto_now=False, auto_now_add=True)
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE)
