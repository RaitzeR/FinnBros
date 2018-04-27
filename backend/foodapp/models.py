from django.db import models

# Create your models here.

class FoodCategory(models.Model):
    title = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

class Food(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image_url = models.CharField(max_length=255, blank=True)
    categories = models.ManyToManyField(FoodCategory, blank=True)
    owner = models.IntegerField(blank=True, default=0)
    street_address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

class UserRating(models.Model):
    rator = models.IntegerField(blank=True)
    rated = models.IntegerField(blank=True)
    rating = models.IntegerField(blank=True)

    def __str__(self):
        return self.title

class Community(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title
