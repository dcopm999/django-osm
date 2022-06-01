""" Urls docstrings go here. """
# -*- coding: utf-8 -*-
from django.urls import include, path

app_name = "osm"

urlpatterns = [
    path("api/", include("osm.api.urls", namespace="osm-api")),
]
