from django.db import models

# Create your models here.

class Carousel(models.Model):
  title = models.CharField(verbose_name='Judul Carousel', max_length=255, default='')
  desc = models.TextField(verbose_name='Deskripsi Carousel', help_text='masukkan deskripsi yang singkat padat dan jelas (usahakan tidak terlalu panjang)', max_length=255, default='')
  background = models.ImageField(verbose_name='Foto Background', upload_to='static/assets/images/carousel/%Y/%m/%d', default='')

  def __str__(self):
    return f'{self.title}'

class Client(models.Model):
  name = models.CharField(verbose_name='Nama Perusahaan Client', default='', blank=True, max_length=255)
  logo = models.ImageField(verbose_name='Logo Client', upload_to='static/assets/images/clients/%Y/%m/%d', default='')
  web = models.URLField(verbose_name='Website Client', help_text='masukkan url website client, beri # jika tidak ada)', max_length=500, default='#', blank=True)

  def __str__(self):
    return f'{self.name}'

class Social_Media(models.Model):
  link = models.URLField(verbose_name='Link Social Media', max_length=500, default='')
  logo = models.CharField(verbose_name='Logo Social Media', help_text='sumber logo dari https://fontawesome.com/v4.7/icons/ contoh: <i class="fa fa-instagram" aria-hidden="true"></i>', max_length=255, default='')