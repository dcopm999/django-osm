# from rest_framework_gis.filterset import GeoFilterSet
from django.contrib.gis.db.models import MultiPolygonField
from django_filters import rest_framework as filters
from rest_framework_gis.filters import GeometryFilter

from osm import models

# '69.279737,41.311273'


class ContainsPointFilter(filters.FilterSet):
    class Meta:
        model = models.World
        fields = "__all__"
        filter_overrides = {
            MultiPolygonField: {
                "filter_class": GeometryFilter,
                "extra": lambda f: {
                    "lookup_expr": "contains",
                },
            }
        }
