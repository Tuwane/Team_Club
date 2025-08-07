from django.template import loader
from django.http import HttpResponse
# Create your views here.
def players(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
