# -*- coding: utf-8 -*-
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from osm import views_api

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("world", views_api.WorldViewSet, basename="world")
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


app_name = "osm"
urlpatterns = router.urls
