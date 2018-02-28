from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.

class CategoryTestClass(TestCase):
    #set up method
    def setUp(self):
        self.nature = Category(category_name="nature")

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nature,Category))

class LocationTestClass(TestCase):
    #set up method
    def setUp(self):
        self.tsavo = Location(place="Tsavo")

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.tsavo,Location))


class ImageTestClass(TestCase):
    def setUp(self):

        self.elephant = Image(name="Elephant",description="It is super big")
        self.elephant.save()

        #creating new category and saving it
        self.nature = Category(category_name="nature")
        self.nature.save()

        #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.elephant,Image))

        #creating new location and saving it
        self.tsavo = Location(place="Tsavo")
        self.tsavo.save()

        self.elephant.location.add(self.tsavo)
        self.elephant.category.add(self.nature)

