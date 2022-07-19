from django.db import models


class Place(models.Model):
    """Место"""
    title = models.CharField(verbose_name='Заголовок',
                             max_length=200,
                             blank=True)
    description_short = models.CharField(verbose_name='Короткое описание',
                                         max_length=200,
                                         blank=True)
    description_long = models.TextField(verbose_name='Длинное описание',
                                        blank=True,
                                        null=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return f'{self.title}'
