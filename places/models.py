from pathlib import Path

from django.db import models


def get_upload_path(instance, filename):
    return Path(instance.place.title) / filename


class Place(models.Model):
    """Место"""
    title = models.CharField(verbose_name='Заголовок',
                             max_length=200,
                             unique=True)
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


class Image(models.Model):
    """Фотография"""
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to=get_upload_path,
    )
    place = models.ForeignKey(
        'Place',
        verbose_name='Место',
        related_name="images",
        on_delete=models.CASCADE,
    )
    order = models.PositiveIntegerField(verbose_name='Порядок',
                                        blank=True,
                                        default=0)

    class Meta:
        ordering = ["-order"]

    def __str__(self):
        return f'{self.order} - ФОТО - {self.place.title}'
