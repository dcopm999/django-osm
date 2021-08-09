from django_elasticsearch_dsl_drf import constants, filter_backends
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework_gis.pagination import GeoJsonPagination

from osm import documents, filters, models, serializers


class CountryListAPIView(generics.ListAPIView):
    queryset = models.Country.objects.filter(deleted=False)
    serializer_class = serializers.CountrySerializer
    filter_backends = [
        filters.PointDistFilter,
        filters.PointIntersectsFilter,
        filters.PointContainsFiltter,
    ]
    pagination_class = GeoJsonPagination


class BuildingListAPIView(generics.ListAPIView):
    queryset = models.Building.objects.filter(deleted=False)
    serializer_class = serializers.BuildingSerializer
    filter_backends = [
        filters.PointDistFilter,
        filters.PointIntersectsFilter,
        filters.PointContainsFiltter,
        DjangoFilterBackend,
    ]
    filterset_fields = ("fclass",)
    pagination_class = GeoJsonPagination


class LanduseListAPIView(generics.ListAPIView):
    queryset = models.Landuse.objects.filter(deleted=False)
    serializer_class = serializers.LanduseSerializer
    filter_backends = [
        filters.PointDistFilter,
        filters.PointIntersectsFilter,
        filters.PointContainsFiltter,
        DjangoFilterBackend,
    ]
    filterset_fields = ("fclass",)
    pagination_class = GeoJsonPagination


class NaturalListAPIView(generics.ListAPIView):
    queryset = models.Natural.objects.filter(deleted=False)
    serializer_class = serializers.NaturalSerializer
    filter_backends = [
        filters.PointDistFilter,
        filters.PointIntersectsFilter,
        filters.PointContainsFiltter,
        DjangoFilterBackend,
    ]
    filterset_fields = ("fclass",)
    pagination_class = GeoJsonPagination


class NaturalAListAPIView(generics.ListAPIView):
    queryset = models.NaturalA.objects.filter(deleted=False)
    serializer_class = serializers.NaturalASerializer
    filter_backends = [
        filters.PointDistFilter,
        filters.PointIntersectsFilter,
        filters.PointContainsFiltter,
        DjangoFilterBackend,
    ]
    filterset_fields = ("fclass",)
    pagination_class = GeoJsonPagination


class PlaceListAPIView(generics.ListAPIView):
    queryset = models.Place.objects.filter(deleted=False)
    serializer_class = serializers.PlaceSerializer
    filter_backends = [
        filters.PointDistFilter,
        filters.PointIntersectsFilter,
        filters.PointContainsFiltter,
        DjangoFilterBackend,
    ]
    filterset_fields = ("fclass",)
    pagination_class = GeoJsonPagination


class PlaceAListAPIView(generics.ListAPIView):
    queryset = models.PlaceA.objects.filter(deleted=False)
    serializer_class = serializers.PlaceASerializer
    filter_backends = [
        filters.PointDistFilter,
        filters.PointIntersectsFilter,
        filters.PointContainsFiltter,
        DjangoFilterBackend,
    ]
    filterset_fields = ("fclass",)
    pagination_class = GeoJsonPagination


class PofwListAPIView(generics.ListAPIView):
    queryset = models.Pofw.objects.filter(deleted=False)
    serializer_class = serializers.PofwSerializer
    filter_backends = [
        filters.PointDistFilter,
        filters.PointIntersectsFilter,
        filters.PointContainsFiltter,
        DjangoFilterBackend,
    ]
    filterset_fields = ("fclass",)
    pagination_class = GeoJsonPagination


class PofwAListAPIView(generics.ListAPIView):
    queryset = models.PofwA.objects.filter(deleted=False)
    serializer_class = serializers.PofwASerializer
    filter_backends = [
        filters.PointDistFilter,
        filters.PointIntersectsFilter,
        filters.PointContainsFiltter,
        DjangoFilterBackend,
    ]
    filterset_fields = ("fclass",)
    pagination_class = GeoJsonPagination


class PoisListAPIView(generics.ListAPIView):
    queryset = models.Pois.objects.filter(deleted=False)
    serializer_class = serializers.PoisSerializer
    filter_backends = [
        filters.PointDistFilter,
        filters.PointIntersectsFilter,
        filters.PointContainsFiltter,
        DjangoFilterBackend,
    ]
    filterset_fields = ("fclass",)
    pagination_class = GeoJsonPagination


class PoisAListAPIView(generics.ListAPIView):
    queryset = models.PoisA.objects.filter(deleted=False)
    serializer_class = serializers.PoisASerializer
    filter_backends = [
        filters.PointDistFilter,
        filters.PointIntersectsFilter,
        filters.PointContainsFiltter,
        DjangoFilterBackend,
    ]
    filterset_fields = ("fclass",)
    pagination_class = GeoJsonPagination


class RailWayListAPIView(generics.ListAPIView):
    queryset = models.RailWay.objects.filter(deleted=False)
    serializer_class = serializers.RailWaySerializer
    filter_backends = [
        filters.PointDistFilter,
        filters.PointIntersectsFilter,
        filters.PointContainsFiltter,
        DjangoFilterBackend,
    ]
    filterset_fields = ("fclass",)
    pagination_class = GeoJsonPagination


class RoadListAPIView(generics.ListAPIView):
    queryset = models.Road.objects.filter(deleted=False)
    serializer_class = serializers.RoadSerializer
    filter_backends = [
        filters.PointDistFilter,
        filters.PointIntersectsFilter,
        filters.PointContainsFiltter,
        DjangoFilterBackend,
    ]
    filterset_fields = ("fclass",)
    pagination_class = GeoJsonPagination


class TrafficListAPIView(generics.ListAPIView):
    queryset = models.Traffic.objects.filter(deleted=False)
    serializer_class = serializers.TrafficSerializer
    filter_backends = [
        filters.PointDistFilter,
        filters.PointIntersectsFilter,
        filters.PointContainsFiltter,
        DjangoFilterBackend,
    ]
    filterset_fields = ("fclass",)
    pagination_class = GeoJsonPagination


class TrafficAListAPIView(generics.ListAPIView):
    queryset = models.TrafficA.objects.filter(deleted=False)
    serializer_class = serializers.TrafficASerializer
    filter_backends = [
        filters.PointDistFilter,
        filters.PointIntersectsFilter,
        filters.PointContainsFiltter,
        DjangoFilterBackend,
    ]
    filterset_fields = ("fclass",)
    pagination_class = GeoJsonPagination


class TransportListAPIView(generics.ListAPIView):
    queryset = models.Transport.objects.filter(deleted=False)
    serializer_class = serializers.TransportSerializer
    filter_backends = [
        filters.PointDistFilter,
        filters.PointIntersectsFilter,
        filters.PointContainsFiltter,
        DjangoFilterBackend,
    ]
    filterset_fields = ("fclass",)
    pagination_class = GeoJsonPagination


class TransportAListAPIView(generics.ListAPIView):
    queryset = models.TransportA.objects.filter(deleted=False)
    serializer_class = serializers.TrafficASerializer
    filter_backends = [
        filters.PointDistFilter,
        filters.PointIntersectsFilter,
        filters.PointContainsFiltter,
        DjangoFilterBackend,
    ]
    filterset_fields = ("fclass",)
    pagination_class = GeoJsonPagination


class WaterListAPIView(generics.ListAPIView):
    queryset = models.Water.objects.filter(deleted=False)
    serializer_class = serializers.WaterSerializer
    filter_backends = [
        filters.PointDistFilter,
        filters.PointIntersectsFilter,
        filters.PointContainsFiltter,
        DjangoFilterBackend,
    ]
    filterset_fields = ("fclass",)
    pagination_class = GeoJsonPagination


class WaterWayListAPIView(generics.ListAPIView):
    queryset = models.WaterWay.objects.filter(deleted=False)
    serializer_class = serializers.WaterWaySerializer
    filter_backends = [
        filters.PointDistFilter,
        filters.PointIntersectsFilter,
        filters.PointContainsFiltter,
        DjangoFilterBackend,
    ]
    filterset_fields = ("fclass",)
    pagination_class = GeoJsonPagination


class NaturalDocumentListAPIView(DocumentViewSet):
    document = documents.NaturalDocument
    serializer_class = serializers.NaturalDocumentSerializer
    lookup_field = "id"
    filter_backends = [filters.PointDistFilter]
    pagination_class = GeoJsonPagination


class PoisDocumentListAPIView(DocumentViewSet):
    document = documents.PoisDocument
    serializer_class = serializers.PoisDocumentSerializer
    lookup_field = "id"
    filter_backends = [
        filter_backends.GeoSpatialFilteringFilterBackend,
    ]
    geo_spatial_filter_fields = {
        "geom": {
            "lookups": [
                constants.LOOKUP_FILTER_GEO_SHAPE,
            ],
        },
    }
