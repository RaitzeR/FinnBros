from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

class FoodPost(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image_url = models.CharField(max_length=255, blank=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title
