from django_elasticsearch_dsl_drf import constants, filter_backends
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework_gis.pagination import GeoJsonPagination

from osm import documents, models, serializers
from osm.filters import ContainsPointFilter


class WorldViewSet(viewsets.ModelViewSet):
    queryset = models.World.objects.all()
    serializer_class = serializers.WorldSerializer
    pagination_class = GeoJsonPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ContainsPointFilter


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = models.Building.objects.all()
    serializer_class = serializers.BuildingSerializer
    pagination_class = GeoJsonPagination


class LanduseViewSet(viewsets.ModelViewSet):
    queryset = models.Landuse.objects.all()
    serializer_class = serializers.LanduseSerializer
    pagination_class = GeoJsonPagination


class NaturalViewSet(viewsets.ModelViewSet):
    queryset = models.Natural.objects.all()
    serializer_class = serializers.NaturalSerializer
    pagination_class = GeoJsonPagination


class NaturalAViewSet(viewsets.ModelViewSet):
    queryset = models.NaturalA.objects.all()
    serializer_class = serializers.NaturalASerializer
    pagination_class = GeoJsonPagination


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceSerializer
    pagination_class = GeoJsonPagination


class PlaceAViewSet(viewsets.ModelViewSet):
    queryset = models.PlaceA.objects.all()
    serializer_class = serializers.PlaceASerializer
    pagination_class = GeoJsonPagination


class PofwViewSet(viewsets.ModelViewSet):
    queryset = models.Pofw.objects.all()
    serializer_class = serializers.PofwSerializer
    pagination_class = GeoJsonPagination


class PofwAViewSet(viewsets.ModelViewSet):
    queryset = models.PofwA.objects.all()
    serializer_class = serializers.PofwASerializer
    pagination_class = GeoJsonPagination


class PoisViewSet(viewsets.ModelViewSet):
    queryset = models.Pois.objects.all()
    serializer_class = serializers.PoisSerializer
    pagination_class = GeoJsonPagination


class PoisAViewSet(viewsets.ModelViewSet):
    queryset = models.PoisA.objects.all()
    serializer_class = serializers.PoisASerializer
    pagination_class = GeoJsonPagination


class RailWayViewSet(viewsets.ModelViewSet):
    queryset = models.RailWay.objects.all()
    serializer_class = serializers.RailWaySerializer
    pagination_class = GeoJsonPagination


class RoadViewSet(viewsets.ModelViewSet):
    queryset = models.Road.objects.all()
    serializer_class = serializers.RoadSerializer
    pagination_class = GeoJsonPagination


class TrafficViewSet(viewsets.ModelViewSet):
    queryset = models.Traffic.objects.all()
    serializer_class = serializers.TrafficSerializer
    pagination_class = GeoJsonPagination


class TrafficAViewSet(viewsets.ModelViewSet):
    queryset = models.TrafficA.objects.all()
    serializer_class = serializers.TrafficASerializer
    pagination_class = GeoJsonPagination


class TransportViewSet(viewsets.ModelViewSet):
    queryset = models.Transport.objects.all()
    serializer_class = serializers.TransportSerializer
    pagination_class = GeoJsonPagination


class TransportAViewSet(viewsets.ModelViewSet):
    queryset = models.TransportA.objects.all()
    serializer_class = serializers.TrafficASerializer
    pagination_class = GeoJsonPagination


class WaterViewSet(viewsets.ModelViewSet):
    queryset = models.Water.objects.all()
    serializer_class = serializers.WaterSerializer
    pagination_class = GeoJsonPagination


class WaterWayViewSet(viewsets.ModelViewSet):
    queryset = models.WaterWay.objects.all()
    serializer_class = serializers.WaterWaySerializer
    pagination_class = GeoJsonPagination


class NaturalDocumentViewSet(DocumentViewSet):
    document = documents.NaturalDocument
    serializer_class = serializers.NaturalDocumentSerializer
    lookup_field = "id"


class PoisDocumentViewSet(DocumentViewSet):
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
