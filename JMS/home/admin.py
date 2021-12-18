from django.contrib import admin
from .models import Client, Carousel, Social_Media

# Register your models here.

admin.site.register(Carousel)
admin.site.register(Client)
admin.site.register(Social_Media)