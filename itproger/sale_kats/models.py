from django.db import models

# Create your models here.
class Articles(models.Model):
    titel = models.CharField('Имя котика', max_length=50)
    anons = models.CharField('Краткое описание', max_length=250)
    full_text = models.TextField('Полное описание')
    date = models.DateTimeField ('Дата публикации')
    image = models.ImageField('Изображение', upload_to='products/')

    # image = models.ImageField('Изображение', upload_to='images/')

    def __str__(self):
        return self.titel

    class Meta:
        verbose_name = 'Котик'
        verbose_name_plural = 'Котики'