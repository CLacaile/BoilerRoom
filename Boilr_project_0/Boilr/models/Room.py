from django.db import models

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    surface = models.FloatField()
    # sensor_set is added autom by django

    def __str__(self):
        return self.name


