from django.contrib import admin
from .models import FirebaseUser, FoodCategory, Food, UserRating, Community

admin.site.register(FirebaseUser)
admin.site.register(FoodCategory)
admin.site.register(Food)
admin.site.register(UserRating)
admin.site.register(Community)
