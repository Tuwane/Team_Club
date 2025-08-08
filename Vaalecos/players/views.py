from django.template import loader
from django.http import HttpResponse
from .models import Player
# Create your views here.
def players(request):
    myplayers = Player.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'myplayers': myplayers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    myplayers = Player.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myplayers': myplayers,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
