from django.db import models
from django.db.models import Count
from django.db.models import Avg
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    category =  models.ForeignKey(Category, on_delete=models.CASCADE)    
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    """  average_rating = Review.objects.filter(restaurant__name=name).aggregate(Avg('rating'))
    number_of_reviews =  Review.objects.filter(restaurant__name=name).count() """
    def __str__(self):
        return self.name + ' - ' + self.address

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    experience_text = models.CharField(max_length=10000)
    def __str__(self):
        return self.experience_text