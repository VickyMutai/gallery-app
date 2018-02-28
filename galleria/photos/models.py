from django.db import models

# Create your models here.
class Location(models.Model):
    place = models.CharField(max_length = 30)

    def __str__(self):
        return self.place

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    image_url = models.ImageField(upload_to = 'categories/',null=True,blank=True)
    location = models.ManyToManyField(Location)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()