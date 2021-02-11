# -*- coding: utf-8 -*-
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


class Building(models.Model):
    osm_id = models.CharField(
        max_length=10, unique=True, db_index=True, verbose_name=_("OSM ID")
    )
    code = models.IntegerField(verbose_name=_("Code"))
    fclass = models.CharField(max_length=28, verbose_name=_("Object class"))

    name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Name")
    )
    type = models.CharField(
        max_length=20, null=True, blank=True, verbose_name=_("Object Type")
    )
    geom = models.PolygonField()

    @staticmethod
    def mapping():
        return {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "type": "type",
            "geom": "POLYGON",
        }

    class Meta:
        verbose_name = _("Building")
        verbose_name_plural = _("Buildings")
        app_label = "osm"


class Landuse(models.Model):
    osm_id = models.CharField(
        max_length=10, unique=True, db_index=True, verbose_name=_("OSM ID")
    )
    code = models.IntegerField(verbose_name=_("Code"))
    fclass = models.CharField(max_length=28, verbose_name=_("Object class"))
    name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Name")
    )
    geom = models.MultiPolygonField()

    @staticmethod
    def mapping():
        return {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }

    class Meta:
        verbose_name = _("Landuse")
        verbose_name_plural = _("Landuses")
        app_label = "osm"


class Natural(models.Model):
    osm_id = models.CharField(
        max_length=10, unique=True, db_index=True, verbose_name=_("OSM ID")
    )
    code = models.IntegerField(verbose_name=_("Code"))
    fclass = models.CharField(max_length=28, verbose_name=_("Object class"))
    name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Name")
    )
    # geom = models.MultiPointField()
    geom = models.PointField()

    @staticmethod
    def mapping():
        return {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "POINT",
            # "geom": "MULTIPOINT",
        }

    class Meta:
        verbose_name = _("Natural")
        verbose_name_plural = _("Naturals")
        app_label = "osm"


class NaturalA(models.Model):
    osm_id = models.CharField(
        max_length=10, unique=True, db_index=True, verbose_name=_("OSM ID")
    )
    code = models.IntegerField(verbose_name=_("Code"))
    fclass = models.CharField(max_length=28, verbose_name=_("Object class"))
    name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Name")
    )
    geom = models.MultiPolygonField()

    @staticmethod
    def mapping():
        return {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }

    class Meta:
        verbose_name = _("Natural A")
        verbose_name_plural = _("Naturals A")
        app_label = "osm"


class Place(models.Model):
    osm_id = models.CharField(
        max_length=10, unique=True, db_index=True, verbose_name=_("OSM ID")
    )
    code = models.IntegerField(verbose_name=_("Code"))
    fclass = models.CharField(max_length=28, verbose_name=_("Object class"))
    population = models.BigIntegerField()
    name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Name")
    )
    geom = models.MultiPointField()

    @staticmethod
    def mapping():
        return {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "population": "population",
            "name": "name",
            "geom": "MULTIPOINT",
        }

    class Meta:
        verbose_name = _("Place")
        verbose_name_plural = _("Places")
        app_label = "osm"


class PlaceA(models.Model):
    osm_id = models.CharField(
        max_length=10, unique=True, db_index=True, verbose_name=_("OSM ID")
    )
    code = models.IntegerField(verbose_name=_("Code"))
    fclass = models.CharField(max_length=28, verbose_name=_("Object class"))
    population = models.BigIntegerField()
    name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Name")
    )
    geom = models.MultiPolygonField()

    @staticmethod
    def mapping():
        return {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "population": "population",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }

    class Meta:
        verbose_name = _("Place A")
        verbose_name_plural = _("Places A")
        app_label = "osm"


class Pofw(models.Model):
    osm_id = models.CharField(
        max_length=10, unique=True, db_index=True, verbose_name=_("OSM ID")
    )
    code = models.IntegerField(verbose_name=_("Code"))
    fclass = models.CharField(max_length=28, verbose_name=_("Object class"))
    name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Name")
    )
    geom = models.MultiPointField()

    @staticmethod
    def mapping():
        return {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOINT",
        }

    class Meta:
        verbose_name = _("Pofw")
        verbose_name_plural = _("Pofws")
        app_label = "osm"


class PofwA(models.Model):
    osm_id = models.CharField(
        max_length=10, unique=True, db_index=True, verbose_name=_("OSM ID")
    )
    code = models.IntegerField(verbose_name=_("Code"))
    fclass = models.CharField(max_length=28, verbose_name=_("Object class"))
    name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Name")
    )
    geom = models.MultiPolygonField()

    @staticmethod
    def mapping():
        return {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }

    class Meta:
        verbose_name = _("Pofw A")
        verbose_name_plural = _("Pofws A")
        app_label = "osm"


class Pois(models.Model):
    osm_id = models.CharField(
        max_length=10, unique=True, db_index=True, verbose_name=_("OSM ID")
    )
    code = models.IntegerField(verbose_name=_("Code"))
    fclass = models.CharField(max_length=28, verbose_name=_("Object class"))
    name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Name")
    )
    geom = models.PointField()

    @staticmethod
    def mapping():
        return {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "POINT",
        }

    class Meta:
        verbose_name = _("Pois")
        verbose_name_plural = _("Poises")
        app_label = "osm"


class PoisA(models.Model):
    osm_id = models.CharField(
        max_length=10, unique=True, db_index=True, verbose_name=_("OSM ID")
    )
    code = models.IntegerField(verbose_name=_("Code"))
    fclass = models.CharField(max_length=28, verbose_name=_("Object class"))
    name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Name")
    )
    geom = models.MultiPolygonField()

    @staticmethod
    def mapping():
        return {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }

    class Meta:
        verbose_name = _("Pois A")
        verbose_name_plural = _("Poises A")
        app_label = "osm"


class RailWay(models.Model):
    osm_id = models.CharField(
        max_length=10, unique=True, db_index=True, verbose_name=_("OSM ID")
    )
    code = models.IntegerField(verbose_name=_("Code"))
    fclass = models.CharField(max_length=28, verbose_name=_("Object class"))
    name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Name")
    )
    layer = models.BigIntegerField(verbose_name=_("Layer"))
    bridge = models.CharField(max_length=1, verbose_name=_("Bridge"))
    tunnel = models.CharField(max_length=1, verbose_name=_("Tunnel"))
    geom = models.MultiLineStringField()

    @staticmethod
    def mapping():
        return {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "layer": "layer",
            "bridge": "bridge",
            "tunnel": "tunnel",
            "geom": "MULTILINESTRING",
        }

    class Meta:
        verbose_name = _("RailWay")
        verbose_name_plural = _("RailWays")
        app_label = "osm"


class Road(models.Model):
    osm_id = models.CharField(
        max_length=10, unique=True, db_index=True, verbose_name=_("OSM ID")
    )
    code = models.IntegerField(verbose_name=_("Code"))
    fclass = models.CharField(max_length=28, verbose_name=_("Object class"))
    name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Object name")
    )
    ref = models.CharField(max_length=20, null=True, verbose_name=_("Ref"))
    oneway = models.CharField(max_length=1, verbose_name=_("One way"))
    maxspeed = models.IntegerField(verbose_name=_("Max speed"))
    layer = models.BigIntegerField(verbose_name=_("Layer"))
    bridge = models.CharField(max_length=1, verbose_name=_("Bridge"))
    tunnel = models.CharField(max_length=1, verbose_name=_("Tunnel"))
    geom = models.MultiLineStringField()

    @staticmethod
    def mapping():
        return {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "ref": "ref",
            "oneway": "oneway",
            "maxspeed": "maxspeed",
            "layer": "layer",
            "bridge": "bridge",
            "tunnel": "tunnel",
            "geom": "MULTILINESTRING",
        }

    class Meta:
        verbose_name = _("Road")
        verbose_name_plural = _("Roads")
        app_label = "osm"


class Traffic(models.Model):
    osm_id = models.CharField(
        max_length=10, unique=True, db_index=True, verbose_name=_("OSM ID")
    )
    code = models.IntegerField(verbose_name=_("Code"))
    fclass = models.CharField(max_length=28, verbose_name=_("Object class"))
    name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Object name")
    )
    geom = models.MultiPointField()

    @staticmethod
    def mapping():
        return {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOINT",
        }

    class Meta:
        verbose_name = _("Traffic")
        verbose_name_plural = _("Traffics")
        app_label = "osm"


class TrafficA(models.Model):
    osm_id = models.CharField(
        max_length=10, unique=True, db_index=True, verbose_name=_("OSM ID")
    )
    code = models.IntegerField(verbose_name=_("Code"))
    fclass = models.CharField(max_length=28, verbose_name=_("Object class"))
    name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Object name")
    )
    geom = models.MultiPolygonField()

    @staticmethod
    def mapping():
        return {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }

    class Meta:
        verbose_name = _("Traffic A")
        verbose_name_plural = _("Traffics A")
        app_label = "osm"


class Transport(models.Model):
    osm_id = models.CharField(
        max_length=10, unique=True, db_index=True, verbose_name=_("OSM ID")
    )
    code = models.IntegerField(verbose_name=_("Code"))
    fclass = models.CharField(max_length=28, verbose_name=_("Object class"))
    name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Object name")
    )
    geom = models.MultiPointField()

    @staticmethod
    def mapping():
        return {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOINT",
        }

    class Meta:
        verbose_name = _("Transport")
        verbose_name_plural = _("Transports")
        app_label = "osm"


class TransportA(models.Model):
    osm_id = models.CharField(
        max_length=10, unique=True, db_index=True, verbose_name=_("OSM ID")
    )
    code = models.IntegerField(verbose_name=_("Code"))
    fclass = models.CharField(max_length=28, verbose_name=_("Object class"))
    name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Object name")
    )
    geom = models.MultiPolygonField()

    @staticmethod
    def mapping():
        return {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }

    class Meta:
        verbose_name = _("Transport A")
        verbose_name_plural = _("Transports A")
        app_label = "osm"


class Water(models.Model):
    osm_id = models.CharField(
        max_length=10, unique=True, db_index=True, verbose_name=_("OSM ID")
    )
    code = models.IntegerField(verbose_name=_("Code"))
    fclass = models.CharField(max_length=28, verbose_name=_("Object class"))
    name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Object name")
    )
    geom = models.MultiPolygonField()

    @staticmethod
    def mapping():
        return {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }

    class Meta:
        verbose_name = _("Water")
        verbose_name_plural = _("Waters")
        app_label = "osm"


class WaterWay(models.Model):
    osm_id = models.CharField(
        max_length=10, unique=True, db_index=True, verbose_name=_("OSM ID")
    )
    code = models.IntegerField(verbose_name=_("Code"))
    fclass = models.CharField(max_length=28, verbose_name=_("Object class"))
    width = models.IntegerField()
    name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Object name")
    )
    geom = models.MultiLineStringField()

    def mapping():
        return {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "width": "width",
            "name": "name",
            "geom": "MULTILINESTRING",
        }

    class Meta:
        verbose_name = _("Water Way")
        verbose_name_plural = _("WaterWays")
        app_label = "osm"
