from typing import Dict

from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from osm import models


@registry.register_document
class NaturalDocument(Document):
    geom = fields.GeoPointField(attr="geom")

    def prepare_geom(self, instance: models.Natural) -> Dict:
        return instance.geom.coords
        # return {
        #    'lon': instance.geom.x,
        #    'lat': instance.geom.y
        # }

    class Django:
        model = models.Natural
        fields = [
            "id",
            "osm_id",
            "code",
            "fclass",
            "name",
        ]

    class Index:
        name = "natural"


@registry.register_document
class PoisDocument(Document):
    geom = fields.GeoPointField(attr="geom")

    def prepare_geom(self, instance: models.Natural) -> Dict:
        return instance.geom.coords
        # return {
        #    'lon': instance.geom.x,
        #    'lat': instance.geom.y
        # }

    class Django:
        model = models.Pois
        fields = [
            "id",
            "osm_id",
            "code",
            "fclass",
            "name",
        ]

    class Index:
        name = "pois"
