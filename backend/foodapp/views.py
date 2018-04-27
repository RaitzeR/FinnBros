from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    return render(request, 'index.html', {

    })

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class LinksPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'links.html', context=None)
