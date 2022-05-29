from django.db import models

# Create your models here.
class Vehicle(models.Model):
    #regexp if necessary
    plate=models.CharField(max_length=10)

    def __str__(self):
        return self.plate


class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    datetime = models.DateTimeField('last_point')
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f'Id = {self.id}, datetime = {self.datetime}, latitude = {self.latitude}, longitude = {self.longitude}'
