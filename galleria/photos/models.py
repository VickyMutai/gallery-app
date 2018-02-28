from django.db import models

# Create your models here.
class Location(models.Model):
    place = models.CharField(max_length = 30)

    def __str__(self):
        return self.place

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name
