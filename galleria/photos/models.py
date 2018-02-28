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

class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    image_url = models.ImageField(upload_to = 'categories/',null=True,blank=True)
    location = models.ManyToManyField(Location)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
