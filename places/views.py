from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from .models import Place


def index(request):
    places = Place.objects.all()
    places_on_map = {
        "type": "FeatureCollection",
        "features": []
    }
    for place in places:
        places_on_map.get("features").append(
            {
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
        )
    context = {"places_on_map": places_on_map}
    return render(request, "places/index.html", context=context)


def get_place_by_id(request, place_id):
    current_place = get_object_or_404(Place, id=place_id)
    response = {
        "title": current_place.title,
        "imgs": [image.image.url for image in current_place.images.all()],
        "description_short": current_place.description_short,
        "description_long": current_place.description_long,
        "coordinates": {
            "lng": current_place.lng,
            "lat": current_place.lat
        }
    }
    return JsonResponse(response,
                        json_dumps_params={'ensure_ascii': False, 'indent': 2})
