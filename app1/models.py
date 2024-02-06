from django.db import models

# Create your models here.
# class Car(models.Model):
#     brand = models.CharField(max_length=255)
#     model_name = models.CharField(max_length=255)
#     year = models.IntegerField()
#     price = models.IntegerField()
#     mileage = models.IntegerField()

class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name