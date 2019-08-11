from django.db import models

class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    # measure_set attribute is added autom by django
    
    def __str__(self):
        return self.name

