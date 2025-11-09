from django.db import models


class Articles(models.Model):
    titel = models.CharField('Назвоние', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField ('Дата публикации')
    image = models.ImageField('Изображение', upload_to='images/')

    def __str__(self):
        return self.titel

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'