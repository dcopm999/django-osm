# -*- coding: utf-8 -*-
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from osm import views_api

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("building", views_api.BuildingViewSet, basename="Building")
router.register("Natural", views_api.NaturalDocumentViewSet, basename="NaturalDocument")
router.register("Pois", views_api.PoisDocumentViewSet, basename="PoisDocument")

app_name = "osm"
urlpatterns = router.urls
