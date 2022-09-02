from . models import *

def menuinks(request):
    links = Category.objects.all()
    return dict(links=links)