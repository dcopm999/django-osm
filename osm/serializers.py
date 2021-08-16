from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from osm import documents, models


class CountrySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Country
        fields = "__all__"
        geo_field = "geom"


class BuildingSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Building
        fields = "__all__"
        geo_field = "geom"


class LanduseSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Landuse
        fields = "__all__"
        geo_field = "geom"


class NaturalSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Natural
        fields = "__all__"
        geo_field = "geom"


class NaturalASerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.NaturalA
        fields = "__all__"
        geo_field = "geom"


class PlaceSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Place
        fields = "__all__"
        geo_field = "geom"


class PlaceASerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.PlaceA
        fields = "__all__"
        geo_field = "geom"


class PofwSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Pofw
        fields = "__all__"
        geo_field = "geom"


class PofwASerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.PofwA
        fields = "__all__"
        geo_field = "geom"


class PoisSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Pois
        fields = "__all__"
        geo_field = "geom"


class PoisASerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.PoisA
        fields = "__all__"
        geo_field = "geom"


class RailWaySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.RailWay
        fields = "__all__"
        geo_field = "geom"


class RoadSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Road
        fields = "__all__"
        geo_field = "geom"


class TrafficSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Traffic
        fields = "__all__"
        geo_field = "geom"


class TrafficASerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.TrafficA
        fields = "__all__"
        geo_field = "geom"


class TransportSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Transport
        fields = "__all__"
        geo_field = "geom"


class TransportASerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.TransportA
        fields = "__all__"
        geo_field = "geom"


class WaterWaySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.WaterWay
        fields = "__all__"
        geo_field = "geom"


class WaterSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Water
        fields = "__all__"
        geo_field = "geom"


class NaturalDocumentSerializer(DocumentSerializer):
    """Serializer for Natural document."""

    class Meta:
        """Meta options."""

        document = documents.NaturalDocument
        fields = "__all__"


class PoisDocumentSerializer(DocumentSerializer):
    """Serializer for Pois document."""

    class Meta:
        """Meta options."""

        document = documents.PoisDocument
        fields = "__all__"
