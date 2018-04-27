from urllib.parse import urlparse
from .Vision import ImageClasses

def get_referrer_root(request):
    try:
        # If getting from outside heroku, get referrer_root and allow in CORS
        parsed = urlparse(request.META['HTTP_REFERER'])
        referrer_root = parsed.scheme + "://" + parsed.netloc
    except KeyError:
        referrer_root = ""
    return referrer_root

def classify_image(request):
    url = request.GET.get("image_url")
    imageClasses = ImageClasses(image_url=url, threshold="0.5")
    classes = imageClasses.classes
