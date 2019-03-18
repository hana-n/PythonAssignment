from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count
from django.db.models import Avg
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import authenticate
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    category =  models.ForeignKey(Category, on_delete=models.CASCADE)    
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images', null=True, default="", blank="true")
    
    def __str__(self):
        return self.name 
        # + ' - ' + self.address
    def avg_ratings(self):
        return self.reviews.aggregate(
            Avg('rating'),
        )        
    def total_reviews(self):
        return self.reviews.count() 
        
class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name ='reviews')
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])    
    photo = models.ImageField(upload_to='review-photos', null=True, default="", blank="true")    
    experience_text = models.TextField(max_length=10000)
    pub_date = models.DateTimeField('Review Date')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)    
    def __str__(self):
        return self.restaurant.name + ' - ' + self.experience_text
    def get_absolute_url(self):
        return reverse('foodreviews:reviews', args=[str(self.restaurant.id)])  
    def total_likes(self):
        return self.likes.count() 

class Comment(models.Model):
    review = models.ForeignKey('foodreviews.Review', on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField(max_length=10000)
    created_date = models.DateTimeField(default = timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment_text
    def get_absolute_url(self):
        return reverse('foodreviews:reviews', args=[str(self.review.restaurant.id)])  

class Reply(models.Model):
    comment = models.ForeignKey('foodreviews.Comment', on_delete=models.CASCADE, related_name='replies')
    reply_text = models.TextField(max_length=10000)
    reply_date = models.DateTimeField(default = timezone.now)
    replied_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.reply_text
    def get_absolute_url(self):
        return reverse('foodreviews:reviews', args=[str(self.comment.review.restaurant.id)])  

class Like(models.Model):    
    review = models.ForeignKey(Review,on_delete=models.CASCADE, related_name='likes')
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    like_date = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse('foodreviews:reviews', args=[str(self.review.restaurant.id)]) 