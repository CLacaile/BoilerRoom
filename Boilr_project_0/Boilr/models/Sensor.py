from django.db import models

class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)


