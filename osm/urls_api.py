# -*- coding: utf-8 -*-
from django.urls import path

from osm import views_api

app_name = "osm"
urlpatterns = [
    path("country/", views_api.CountryListAPIView.as_view(), name="country-list"),
    path("building/", views_api.BuildingListAPIView.as_view(), name="building-list"),
    path("landuse/", views_api.LanduseListAPIView.as_view(), name="landuse-list"),
    path("natural/", views_api.NaturalListAPIView.as_view(), name="natural-list"),
    path("natural-a/", views_api.NaturalAListAPIView.as_view(), name="natural-a-list"),
    path("place/", views_api.PlaceListAPIView.as_view(), name="place-list"),
    path("place-a/", views_api.PlaceAListAPIView.as_view(), name="place-a-list"),
    path("pofw/", views_api.PofwListAPIView.as_view(), name="pofw-list"),
    path("pofw-a/", views_api.PofwAListAPIView.as_view(), name="pofw-a-list"),
    path("pois/", views_api.PoisListAPIView.as_view(), name="pois-list"),
    path("pois-a/", views_api.PoisAListAPIView.as_view(), name="pois-a-list"),
    path("railway/", views_api.RailWayListAPIView.as_view(), name="railway-list"),
    path("road/", views_api.RoadListAPIView.as_view(), name="road-list"),
    path("traffic/", views_api.TrafficListAPIView.as_view(), name="traffic-list"),
    path("traffic-a/", views_api.TrafficAListAPIView.as_view(), name="traffic-a-list"),
    path("transport/", views_api.TransportListAPIView.as_view(), name="transport-list"),
    path(
        "transport-a/",
        views_api.TransportAListAPIView.as_view(),
        name="transport-a-list",
    ),
    path("water/", views_api.WaterListAPIView.as_view(), name="water-list"),
    path("waterway/", views_api.WaterWayListAPIView.as_view(), name="waterway-list"),
]
