from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from osm import documents, models


class BuildingSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Building
        geo_field = "geom"
        fields = (
            'id',
            'osm_id',
            'code',
            'fclass',
            'name',
            'type',
        )


class NaturalDocumentSerializer(DocumentSerializer):
    """Serializer for Natural document."""
    class Meta:
        """Meta options."""
        document = documents.NaturalDocument
        fields = (
            'id',
            'osm_id',
            'code',
            'fclass',
            'type'
            'name',
            'geom',
        )


class PoisDocumentSerializer(DocumentSerializer):
    """Serializer for Pois document."""
    class Meta:
        """Meta options."""
        document = documents.PoisDocument
        fields = [
            'id',
            'osm_id',
            'code',
            'fclass',
            'type'
            'name',
            'geom',            
        ]
