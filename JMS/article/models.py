from django.db import models
from django.utils.text import slugify

# Create your models here.

class Article(models.Model):
  title = models.CharField(verbose_name='Title', max_length=255, default='')
  thumbnail = models.ImageField(verbose_name='Thumbnail', upload_to='static/blog/assets/img/static/thumbnail/%Y/%m/%d', default='')
  content = models.TextField(verbose_name='Content', max_length=100000, default='')
  published = models.DateTimeField(editable=True)
  updated = models.DateTimeField(auto_now=True)
  slug = models.SlugField(editable=False, blank=True)

  class Meta:
    verbose_name_plural = 'Artikel'

  def save(self):
    self.slug = slugify(self.title)
    super(Article, self).save()

  def __str__(self):
    return f'{self.title}'