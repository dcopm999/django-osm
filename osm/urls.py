""" Urls docstrings go here. """
# -*- coding: utf-8 -*-
from django.urls import include, path
from django.views.generic import TemplateView

app_name = "tashkent"

urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html")),
    path("api", include("osm.urls_api")),
]
