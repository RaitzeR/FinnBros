from foodapp.models import Food, FoodCategory
from django.http import HttpResponse, JsonResponse

# Attach categories to food post (and creates categories along the way). Front-end gives category names in array
def categories_to_food(request):
    cat_titles = request.GET.get("categories")
    food_id = request.GET.get("food_id")

    cat_titles = cat_titles.split(",")

    for cat in cat_titles:
        post_to_attach = Food.objects.get(pk=int(food_id))
        try:
            cat_to_attach = FoodCategory.objects.get(title=cat)
        except FoodCategory.DoesNotExist:
            cat_to_attach = FoodCategory(title=cat)
            cat_to_attach.save()
        post_to_attach.categories.add(cat_to_attach)

    return HttpResponse(200)

def remove_categories(request):
    cat_titles = request.GET.get("categories")
    food_id = request.GET.get("food_id")
    
    food_object = Food.objects.get(pk=int(food_id))

    cat_titles = cat_titles.split(",")
    for title in cat_titles:
        category_obj = FoodCategory.objects.get(title=title)
        food_object.categories.remove(category_obj)
        food_object.save()

    return HttpResponse(200)
