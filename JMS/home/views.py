from django.shortcuts import render
from django.views.generic import TemplateView
import requests
from article.models import Article
from . import models

# Create your views here.

class index(TemplateView):

  def __init__(self):
    self.context = {
      'title': 'JMS Logistik | PT Jasa Moda Solusi',
      'carousel': models.Carousel.objects.all(),
      'data_home': models.Data_Angka.objects.all()[0],
      'articles': Article.objects.order_by('-published')[0:3],
      'clients': models.Client.objects.all(),
      'social_media': models.Social_Media.objects.all(),
      'home_kurs': [],
      'kurs': []
    }

  def get(self, request):
    url = 'https://api.exchangerate.host/latest?base=IDR&amount=1'
    response = requests.get(url)
    data_list = list(response.json()['rates'].items())

    for i in data_list:
      if i[1] != 0:
        self.context['kurs'].append((i[0], 1 / i[1]))

      if i[0] == 'USD':
        self.context['home_kurs'].append((i[0], 1 / i[1]))
      elif i[0] == 'EUR':
        self.context['home_kurs'].append((i[0], 1 / i[1]))
      elif i[0] == 'CNY':
        self.context['home_kurs'].append((i[0], 1 / i[1]))
      elif i[0] == 'JPY':
        self.context['home_kurs'].append((i[0], 1 / i[1]))
      elif i[0] == 'AUD':
        self.context['home_kurs'].append((i[0], 1 / i[1]))
      elif i[0] == 'SGD':
        self.context['home_kurs'].append((i[0], 1 / i[1]))
      elif i[0] == 'MYR':
        self.context['home_kurs'].append((i[0], 1 / i[1]))

    return render(request, 'home/index.html', self.context)

class kurs(TemplateView):

  def __init__(self):
    self.context = {
      'title': 'Kurs | JMS Logistik | PT Jasa Moda Solusi',
      'social_media': models.Social_Media.objects.all(),
      'kurs': [],
      'kurs_date': None
    }

  def get(self, request):
    url = 'https://api.exchangerate.host/latest?base=IDR&amount=1'
    response = requests.get(url)
    self.context['kurs_date'] = response.json()['date']
    data_list = list(response.json()['rates'].items())

    for i in data_list:
      if i[1] != 0:
        self.context['kurs'].append((i[0], 1 / i[1]))
    
    return render(request, 'home/kurs/index.html', self.context)

class contact(TemplateView):
  
  def __init__(self):
    self.context = {
      'title': 'Kontak | JMS Logistik | PT Jasa Moda Solusi'
    }

  def get(self, request):
    return render(request, 'home/contact/index.html', self.context)