# -*- coding: utf-8 -*-
from rest_framework.routers import SimpleRouter, DefaultRouter
from django.conf import settings

from osm import api_views

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('building', api_views.BuildingViewSet, basename='Building')
router.register('Natural', api_views.NaturalDocumentViewSet, basename='NaturalDocument')
router.register('Pois', api_views.PoisDocumentViewSet, basename='PoisDocument')

app_name = 'osm'
urlpatterns = router.urls
