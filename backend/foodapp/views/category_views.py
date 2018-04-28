from foodapp.models import Food, FoodCategory
from django.http import HttpResponse, JsonResponse

# Attach categories to food post (and creates categories along the way). Front-end gives category names in array
def categories_to_food(request):
    cat_titles = request.GET.get("categories")
    food_id = request.GET.get("food_id")

    cat_titles = cat_titles.split(",")
    print(cat_titles)

    for cat in cat_titles:
        post_to_attach = Food.objects.get(pk=int(food_id))
        try:
            cat_to_attach = FoodCategory.objects.get(title=cat)
        except FoodCategory.DoesNotExist:
            cat_to_attach = FoodCategory(title=cat)
            cat_to_attach.save()
        post_to_attach.categories.add(cat_to_attach)

    return HttpResponse(200)
