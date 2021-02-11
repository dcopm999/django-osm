from django_elasticsearch_dsl_drf import constants, filter_backends
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from rest_framework import viewsets
from rest_framework_gis.pagination import GeoJsonPagination

from osm import documents, models, serializers


class BuildingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Building.objects.all()
    serializer_class = serializers.BuildingSerializer
    pagination_class = GeoJsonPagination


class NaturalDocumentViewSet(DocumentViewSet):
    document = documents.NaturalDocument
    serializer_class = serializers.NaturalDocumentSerializer


class PoisDocumentViewSet(DocumentViewSet):
    document = documents.PoisDocument
    serializer_class = serializers.PoisDocumentSerializer
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
