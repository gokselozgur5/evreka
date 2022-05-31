from webbrowser import Opera
from django.db import models
from django.forms import DateTimeField

# Create your models here.
class Bin(models.Model):
    #regexp if necessary
    latitude=models.FloatField()
    longitude= models.FloatField()
    collection_frequency = models.IntegerField()
    last_collection = DateTimeField()
#classes could be return one or more attributes. 
    def __str__(self):
        return self.id


class Operation(models.Model):
    #regexp if necessary
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Meta_Operation(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
