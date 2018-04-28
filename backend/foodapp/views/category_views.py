# Attach categories to food post (and creates categories along the way). Front-end gives category names in array
def categories_to_food(request):
    cat_titles = request.GET.getlist("category_titles[]")
    post_id = request.GET.get("post_id")

    for cat in cat_titles:
        post_to_attach = Food.get.objects(pk=int(post_id))
        try:
            cat_to_attach = FoodCategory.objects.get(title=cat)
        except FoodCategory.ObjectNotFound:
            cat_to_attach = Category(title=cat)
            cat_to_attach.save()
        post_to_attach.categories.add(cat_to_attach)
