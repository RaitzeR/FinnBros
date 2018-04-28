from django.db import models

# Create your models here.

class FirebaseUser(models.Model):
    firebase_id = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.firebase_id)

class FoodCategory(models.Model):
    title = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

class Food(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image_url = models.CharField(max_length=255, blank=True)
    categories = models.ManyToManyField(FoodCategory, blank=True)
    user = models.ForeignKey(FirebaseUser, on_delete=models.CASCADE, null=True)
    street_address = models.CharField(max_length=255, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    is_bought = models.BooleanField(default=False)
    buyer = models.IntegerField(blank=True, default=0)

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
    users = models.ManyToManyField(FirebaseUser, blank=True)
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title
