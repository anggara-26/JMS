from django.shortcuts import render
from django.views.generic import TemplateView
from . import models

# Create your views here.

class index(TemplateView):

  def __init__(self):
    self.context = {
      'title': 'JMS Logistik | PT Jasa Moda Solusi',
      'carousel': models.Carousel.objects.all(),
      'clients': models.Client.objects.all(),
      'social_media': models.Social_Media.objects.all()
    }

  def get(self, request):
    return render(request, 'home/index.html', self.context)