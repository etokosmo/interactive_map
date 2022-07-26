from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from .models import Place


def serialize_places(place):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [place.lng, place.lat]
        },
        "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": reverse("place_id", args=[place.id, ])
        }
    }


def index(request):
    places = Place.objects.all()
    places_on_map = {
        "type": "FeatureCollection",
        "features": [serialize_places(place) for place in places]
    }
    context = {"places_on_map": places_on_map, "DEBUG": settings.DEBUG}
    return render(request, "places/index.html", context=context)


def get_place_by_id(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    response = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
