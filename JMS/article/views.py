from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.utils.timezone import localtime
from home.models import Social_Media
from .models import Article

# Create your views here.

class index(TemplateView):

  def __init__(self):
    self.context = {
      'title': 'Artikel | JMS Logistik | PT Jasa Moda Solusi',
      'social_media': Social_Media.objects.all(),
      'articles': None}

  def get(self, request):
    self.context['articles'] = Article.objects.order_by('-published')
    
    return render(request, 'article/index.html', self.context)

class single_blog(TemplateView):

  def __init__(self):
    self.context = {
      'title': '',
      'social_media': Social_Media.objects.all(),
      'article': None}
    self.backredirect = '../../../../'
  
  def get(self, request, *args, **kwargs):
    articles = Article.objects.filter(slug=kwargs.get('articleSlug'))

    def filterArticles(x):
      articles_time = localtime(x.published)
      if articles_time.year == int(kwargs.get('year')) and articles_time.month == int(kwargs.get('month')) and articles_time.day == int(kwargs.get('day')):
        return True
      else:
        return False

    articles = filter(filterArticles, articles)
    articles = list(articles)

    if not articles:
      return redirect(self.backredirect)

    self.context['title'] = f'{articles[0].title} - Artikel | JMS Logistik | PT Jasa Moda Solusi'
    self.context['article'] = articles[0]

    return render(request, 'article/single_article/index.html', self.context)