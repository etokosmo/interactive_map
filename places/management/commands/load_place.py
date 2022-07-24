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


def create_object(response_location: dict) -> Tuple[Place, bool]:
    location, location_created = Place.objects.get_or_create(
        title=response_location.get("title"),
        description_short=response_location.get("description_short"),
        description_long=response_location.get("description_long"),
        lng=response_location.get("coordinates").get("lng"),
        lat=response_location.get("coordinates").get("lat"),
    )

    location_images = response_location.get("imgs")
    upload_photo_in_location(location, location_images)
    return location_created


def upload_photo_in_location(location: Place,
                             location_images: list[str]) -> None:
    for location_image_url in location_images:
        filename, file_extension = get_filename_and_file_extension(
            location_image_url)

        response = requests.get(location_image_url)
        response.raise_for_status()
        uploaded_photo = ContentFile(response.content)

        location_image = Image(place=location)

        location_image.image.save(f'{filename}{file_extension}',
                                  uploaded_photo,
                                  save=True)


class Command(BaseCommand):
    help = 'Create place from url'

    def handle(self, *args, **options):
        url = options['url']

        response = requests.get(url)
        response.raise_for_status()
        response_location = response.json()

        location_created = create_object(response_location)
        if location_created:
            location_title = response_location.get("title")
            logger.info(f"Локация '{location_title}' успешно добавлена")

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            help='json url with location'
        )
