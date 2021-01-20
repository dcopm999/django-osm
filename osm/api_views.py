from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_TERMS,
    LOOKUP_FILTER_RANGE,
    LOOKUP_FILTER_PREFIX,
    LOOKUP_FILTER_WILDCARD,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_EXCLUDE,
    LOOKUP_FILTER_GEO_SHAPE
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
    GeoSpatialFilteringFilterBackend,
)

from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from rest_framework import viewsets
from rest_framework_gis.pagination import GeoJsonPagination

from osm import documents, serializers, models


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
        GeoSpatialFilteringFilterBackend,
    ]
    geo_spatial_filter_fields = {
        'geom': {
            'lookups': [
                LOOKUP_FILTER_GEO_SHAPE,
            ],
        },

    }
