# -*- coding: utf-8 -*-
from django.urls import path

from osm.api import views

app_name = "osm"
urlpatterns = [
    path("country/", views.CountryListAPIView.as_view(), name="country-list"),
    path("building/", views.BuildingListAPIView.as_view(), name="building-list"),
    path("landuse/", views.LanduseListAPIView.as_view(), name="landuse-list"),
    path("natural/", views.NaturalListAPIView.as_view(), name="natural-list"),
    path("naturala/", views.NaturalAListAPIView.as_view(), name="naturala-list"),
    path("place/", views.PlaceListAPIView.as_view(), name="place-list"),
    path("placea/", views.PlaceAListAPIView.as_view(), name="placea-list"),
    path("pofw/", views.PofwListAPIView.as_view(), name="pofw-list"),
    path("pofwa/", views.PofwAListAPIView.as_view(), name="pofwa-list"),
    path("pois/", views.PoisListAPIView.as_view(), name="pois-list"),
    path("poisa/", views.PoisAListAPIView.as_view(), name="poisa-list"),
    path("railway/", views.RailWayListAPIView.as_view(), name="railway-list"),
    path("road/", views.RoadListAPIView.as_view(), name="road-list"),
    path("traffic/", views.TrafficListAPIView.as_view(), name="traffic-list"),
    path("traffica/", views.TrafficAListAPIView.as_view(), name="traffica-list"),
    path("transport/", views.TransportListAPIView.as_view(), name="transport-list"),
    path(
        "transporta/",
        views.TransportAListAPIView.as_view(),
        name="transporta-list",
    ),
    path("water/", views.WaterListAPIView.as_view(), name="water-list"),
    path("waterway/", views.WaterWayListAPIView.as_view(), name="waterway-list"),
]
