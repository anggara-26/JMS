from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import Client, Carousel, Social_Media, Data_Angka

# Register your models here.

admin.site.register(Carousel)
admin.site.register(Client)
admin.site.register(Social_Media)
admin.site.register(Data_Angka, SingletonModelAdmin)