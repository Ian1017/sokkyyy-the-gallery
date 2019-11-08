from django.db import models
from django_countries.fields import CountryField




# Create your models here.
class Location(models.Model):
    country = CountryField(blank="select country")

    @classmethod
    def find_location(cls,country):
        location = cls.objects.filter(country=country)
        return location
    
    def __repr__(self):
        return self.country

class Category(models.Model):
    IMAGE_CATEGORIES = (
        ('travel',"Travel"),
        ('food',"Food"),
        ('places',"Places"),
        ('people','People'),
        ('sports','Sports'),
    )
    category = models.CharField(max_length=20, choices=IMAGE_CATEGORIES)

    @classmethod
    def search_by_category(cls,category):
        category = cls.objects.filter(category =category)
        return category
    
    @classmethod
    def find_category_id(cls,category):
        category = cls.objects.filter(category=category)
        return category

    def __str__(self):
        return self.category

class Image(models.Model):
    image = models.ImageField(upload_to='gallery/')
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='img_category')
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE, related_name='img_location')

    @classmethod
    def search_image(cls,category):
        images = cls.objects.filter(category = category)
        return images
    
    @classmethod
    def filter_by_location(cls,location):
        images = cls.objects.filter(location = location)
        return images


    def __str__(self):
        return self.name




