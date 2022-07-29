import os
from typing import Tuple
from urllib.parse import urlsplit, unquote_plus
import logging

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image

logger = logging.getLogger(__name__)


def get_filename_and_file_extension(url: str) -> Tuple[str, str]:
    """Получаем название файла и расширение файла из ссылки"""
    truncated_url = unquote_plus(
        urlsplit(url, scheme='', allow_fragments=True).path)
    filename, file_extension = os.path.splitext(truncated_url)
    filename = filename.split("/")[-1]
    return filename, file_extension


def create_place(place_response: dict) -> Tuple[Place, bool]:
    place, place_created = Place.objects.get_or_create(
        title=place_response.get("title")
    )
    place.description_short = place_response["description_short"]
    place.description_long = place_response["description_long"]
    place.lat = place_response["coordinates"]["lng"]
    place.lat = place_response["coordinates"]["lat"]

    place_images = place_response.get("imgs")
    upload_photo_in_place(place, place_images)
    return place_created


def upload_photo_in_place(place: Place,
                          place_images: list[str]) -> None:
    for place_image_url in place_images:
        filename, file_extension = get_filename_and_file_extension(
            place_image_url)

        response = requests.get(place_image_url)
        response.raise_for_status()
        uploaded_photo = ContentFile(response.content)

        place_image = Image(place=place)

        place_image.image.save(f'{filename}{file_extension}',
                               uploaded_photo,
                               save=True)


class Command(BaseCommand):
    help = 'Create place from url'

    def handle(self, *args, **options):
        url = options['url']

        response = requests.get(url)
        response.raise_for_status()
        place_response = response.json()

        place_created = create_object(place_response)
        if place_created:
            place_title = place_response.get("title")
            logger.info(f"Локация '{place_title}' успешно добавлена")

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            help='json url with place'
        )
