# from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from osm import documents, models


class BuildingSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Building
        geo_field = "geom"
        fields = (
            "id",
            "osm_id",
            "code",
            "fclass",
            "name",
            "type",
        )


class LanduseSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Landuse
        geo_field = "geom"
        fields = "__all__"


class NaturalSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Natural
        geo_field = "geom"
        fields = "__all__"


class NaturalASerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.NaturalA
        geo_field = "geom"
        fields = "__all__"


class PlaceSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Place
        geo_field = "geom"
        fields = "__all__"


class PlaceASerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.PlaceA
        geo_field = "geom"
        fields = "__all__"


class PofwSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Pofw
        geo_field = "geom"
        fields = "__all__"


class PofwASerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.PofwA
        geo_field = "geom"
        fields = "__all__"


class PoisSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Pois
        geo_field = "geom"
        fields = "__all__"


class PoisASerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.PoisA
        geo_field = "geom"
        fields = "__all__"


class RailWaySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.RailWay
        geo_field = "geom"
        fields = "__all__"


class RoadSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Road
        geo_field = "geom"
        fields = "__all__"


class TrafficSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Traffic
        geo_field = "geom"
        fields = "__all__"


class TrafficASerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.TrafficA
        geo_field = "geom"
        fields = "__all__"


class TransportSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Transport
        geo_field = "geom"
        fields = "__all__"


class TransportASerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.TransportA
        geo_field = "geom"
        fields = "__all__"


class WaterWaySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.WaterWay
        geo_field = "geom"
        fields = "__all__"


class WaterSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Water
        geo_field = "geom"
        fields = "__all__"


class NaturalDocumentSerializer(DocumentSerializer):
    """Serializer for Natural document."""

    class Meta:
        """Meta options."""

        document = documents.NaturalDocument
        fields = (
            "id",
            "osm_id",
            "code",
            "fclass",
            "type" "name",
            "geom",
        )


class PoisDocumentSerializer(DocumentSerializer):
    """Serializer for Pois document."""

    class Meta:
        """Meta options."""

        document = documents.PoisDocument
        fields = [
            "id",
            "osm_id",
            "code",
            "fclass",
            "type" "name",
            "geom",
        ]
