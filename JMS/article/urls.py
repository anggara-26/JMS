from django.urls import path, re_path
from .views import index, single_blog

app_name = 'article'
urlpatterns = [
  path('', index.as_view(), name='index'),
  re_path(r'^(?P<year>[\w-]+)/(?P<month>[\w-]+)/(?P<day>[\w-]+)/(?P<articleSlug>[\w-]+)/', single_blog.as_view()),
]