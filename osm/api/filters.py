# '69.279737,41.311273'
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from rest_framework.filters import BaseFilterBackend


class PointDistFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        request_keys = request.GET.keys()
        if "dist" in request_keys and "point" in request_keys:
            dist = float(request.GET["dist"])
            point = request.GET["point"].split(",")
            point = Point(float(point[0]), float(point[1]), srid=4326)
            queryset = (
                queryset.annotate(distance=Distance("geom", point))
                .filter(distance__lte=dist)
                .order_by("distance")
            )
        return queryset


class PointIntersectsFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if "intersects" in request.GET.keys():
            point = request.GET["intersects"].split(",")
            point = Point(float(point[0]), float(point[1]))
            queryset = queryset.filter(geom__intersects=point)
        return queryset


class PointContainsFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if "contains" in request.GET.keys():
            point = request.GET["contains"].split(",")
            point = Point(float(point[0]), float(point[1]))
            queryset = queryset.filter(geom__intersects=point)
        return queryset
