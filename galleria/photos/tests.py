from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.

class CategoryTestClass(TestCase):
    #set up method
    def setUp(self):
        self.nature = Category(category_name="nature")

class LocationTestClass(TestCase):
    #set up method
    def setUp(self):
        self.tsavo = Location(place="Tsavo")

class ImageTestClass(TestCase):
    def setUp(self):

        self.elephant = Image(name="Elephant",description="It is super big")
        self.elephant.save()

        #creating new category and saving it
        self.nature = Category(category_name="nature")
        self.nature.save()

        #creating new location and saving it
        self.tsavo = Location(place="Tsavo")
        self.tsavo.save()

        self.elephant.location.add(self.tsavo)
        self.elephant.category.add(self.nature)

