from django.urls import path

from . import views

urlpatterns = [
    path('<int:place_id>', views.get_place_by_id, name='place_id'),
    path('', views.index, name='places_indexpage'),
]
