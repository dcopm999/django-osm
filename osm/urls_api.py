# -*- coding: utf-8 -*-
from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from osm import views_api

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()
"""
router.register("country", views_api.CountryViewSet, basename="country")
router.register("building", views_api.BuildingViewSet, basename="building")
router.register("landuse", views_api.LanduseViewSet, basename="landuse")
router.register("natural", views_api.NaturalViewSet, basename="natural")
router.register("natural_a", views_api.NaturalAViewSet, basename="natural_a")
router.register("place", views_api.PlaceViewSet, basename="place")
router.register("place_a", views_api.PlaceAViewSet, basename="place_a")
router.register("pofw", views_api.PofwViewSet, basename="pofw")
router.register("pofw_a", views_api.PofwAViewSet, basename="pofw_a")
router.register("pois", views_api.PoisViewSet, basename="pois")
router.register("pois_a", views_api.PoisAViewSet, basename="pois_a")
router.register("railway", views_api.RailWayViewSet, basename="railway")
router.register("road", views_api.RoadViewSet, basename="road")
router.register("traffic", views_api.TrafficViewSet, basename="traffic")
router.register("traffic_a", views_api.TrafficAViewSet, basename="traffic_a")
router.register("transport", views_api.TransportViewSet, basename="transport")
router.register("transport_a", views_api.TransportAViewSet, basename="transport_a")
router.register("water", views_api.WaterViewSet, basename="water")
router.register("waterway", views_api.WaterWayViewSet, basename="waterway")

router.register("search/pois", views_api.PoisDocumentViewSet, basename="pois-search")
router.register(
    "search/natural", views_api.NaturalDocumentViewSet, basename="natural-search"
)
"""

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
# urlpatterns = router.urls
