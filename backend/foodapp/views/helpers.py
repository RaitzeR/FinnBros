from urllib.parse import urlparse


def get_referrer_root(request):
    try:
        print("l6@get_referrer_root")
        print(request.META)
        print("l8@get_referrer_root")
        print(request.META['HTTP_REFERER'])
        # If getting from outside heroku, get referrer_root and allow in CORS
        parsed = urlparse(request.META['HTTP_REFERER'])
        referrer_root = parsed.scheme + "://" + parsed.netloc
    except KeyError:
        referrer_root = ""
    return referrer_root


# Just for testing
def index(request):
    from django.shortcuts import render
    return render(request, 'index.html', {

    })


def get_percentage(price, original_price):
    return round((1 - (price / original_price)) * 100)
