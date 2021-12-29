from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
  path('', views.index.as_view(), name='index'),
  path('kurs/', views.kurs.as_view(), name='kurs'),
  path('kontak/', views.contact.as_view(), name='contact'),
]