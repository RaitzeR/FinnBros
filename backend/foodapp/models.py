from django.db import models

# Create your models here.

class FoodPost(models.Model):
    title = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
