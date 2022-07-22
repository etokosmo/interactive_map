from django.shortcuts import render

from .models import Place


def index(request):
    places = Place.objects.all()
    places_geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for place in places:
        places_geojson.get("features").append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
                }
            }
        )
    context = {"content": places_geojson}
    return render(request, "index.html", context=context)
