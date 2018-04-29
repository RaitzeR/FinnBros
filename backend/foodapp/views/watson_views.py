from foodapp.Vision import ImageClasses
from django.http import HttpResponse, JsonResponse
from foodapp.views.helpers import *
import json

# Give image categories to front-end
def img_categories(request):
    #url = request.GET.get("image_url")
    #import pdb; pdb.set_trace()
    body_unicode = request.body.decode('utf-8')
    print(body_unicode)

    imageClasses = ImageClasses(image_url=url, threshold="0.5")
    classes = imageClasses.classes

    jsonresp = JsonResponse(classes, safe=False)
    print("l13@img_categories")
    print(get_referrer_root(request))
    jsonresp['Access-Control-Allow-Origin'] = get_referrer_root(request)
    print("l16@img_categories")
    print(jsonresp['Access-Control-Allow-Origin'])
    return jsonresp
