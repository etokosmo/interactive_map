import logging
import os
from urllib.parse import urlsplit, unquote_plus

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from requests.exceptions import HTTPError

from places.models import Place, Image

logger = logging.getLogger(__name__)


def get_filename(url: str) -> str:
    """Получаем название файла и расширение файла из ссылки"""
    truncated_url = unquote_plus(
        urlsplit(url, scheme='', allow_fragments=True).path)
    _, filename = os.path.split(truncated_url)
    return filename


def create_place(place_response: dict) -> bool:
    place, place_created = Place.objects.get_or_create(
        title=place_response.get("title"),
        lng=place_response["coordinates"]["lng"],
        lat=place_response["coordinates"]["lat"]
    )
    place.description_short = place_response["description_short"]
    place.description_long = place_response["description_long"]
    place.save()

    place_images = place_response.get("imgs")
    upload_photo_in_place(place, place_images)
    return place_created


def upload_photo_in_place(place: Place,
                          place_images: list[str]) -> None:
    for place_image_url in place_images:
        filename = get_filename(
            place_image_url)

        response = requests.get(place_image_url)
        response.raise_for_status()
        uploaded_photo = ContentFile(response.content)

        place_image = Image(place=place)

        place_image.image.save(filename,
                               uploaded_photo,
                               save=True)


class Command(BaseCommand):
    help = 'Create place from url'

    def handle(self, *args, **options):
        url = options['url']

        response = requests.get(url)
        response.raise_for_status()
        place_response = response.json()
        try:
            place_created = create_place(place_response)
            if place_created:
                place_title = place_response.get("title")
                logger.info(f"Локация '{place_title}' успешно добавлена")
        except KeyError:
            logger.info(f"KeyError. Ошибка в чтении ключей у place_response")
        except HTTPError:
            logger.info(f"HTTPError. Ошибка при скачивании картинки")

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            help='json url with place'
        )
