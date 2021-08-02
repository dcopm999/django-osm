# '69.279737,41.311273'
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from rest_framework.filters import BaseFilterBackend


class DistPointMeterFilter(BaseFilterBackend):
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

    def get_filter_point(self, request, **kwargs):
        point = super().get_filter_point(request, **kwargs)
        return point
