from django.db import models

# Create your models here.
class Slider_first(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='images', verbose_name='Картинка')

    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='images', verbose_name='Картинка')

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    text = models.TextField()
    slug = models.SlugField(max_length=50, unique=True)
    date_add = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog', verbose_name='Capture')

    def __str__(self):
        return (f'{self.title}, {self.date_add}')