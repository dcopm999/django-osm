# -*- coding: utf-8 -*-
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    fips = models.CharField(max_length=2, blank=True, null=True, verbose_name=_("Fips"))
    iso2 = models.CharField(max_length=2, verbose_name=_("iso2"))
    iso3 = models.CharField(max_length=3, verbose_name=_("iso3"))
    un = models.IntegerField(verbose_name=_("UN"))
    name = models.CharField(
        max_length=50, unique=True, db_index=True, verbose_name=_("Name")
    )
    area = models.IntegerField(verbose_name=_("Area"))
    pop2005 = models.BigIntegerField(verbose_name=_("Pop 2005"))
    region = models.IntegerField(verbose_name=_("Region"))
    subregion = models.IntegerField(verbose_name=_("Subregion"))
    lon = models.FloatField(verbose_name=_("Lon"))
    lat = models.FloatField(verbose_name=_("Lat"))
    geom = models.MultiPolygonField(verbose_name=_("Geom"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    deleted = models.BooleanField(default=False, verbose_name=_("Is deleted"))

    @staticmethod
    def mapping():
        return {
            "fips": "FIPS",
            "iso2": "ISO2",
            "iso3": "ISO3",
            "un": "UN",
            "name": "NAME",
            "area": "AREA",
            "pop2005": "POP2005",
            "region": "REGION",
            "subregion": "SUBREGION",
            "lon": "LON",
            "lat": "LAT",
            "geom": "MULTIPOLYGON",
        }

    def __str__(self):
        return f"Country({self.name})"

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")


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
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    deleted = models.BooleanField(default=False, verbose_name=_("Is deleted"))

    def __str__(self):
        return f"Building({self.osm_id})"

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
        ordering = ["-id"]
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
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    deleted = models.BooleanField(default=False, verbose_name=_("Is deleted"))

    def __str__(self):
        return f"Landuse({self.osm_id})"

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
        ordering = ["-id"]
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
    geom = models.PointField()
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    deleted = models.BooleanField(default=False, verbose_name=_("Is deleted"))

    def __str__(self):
        return f"Natural({self.osm_id})"

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
        ordering = ["-id"]
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
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    deleted = models.BooleanField(default=False, verbose_name=_("Is deleted"))

    def __str__(self):
        return f"NaturalA({self.osm_id})"

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
        ordering = ["-id"]
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
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    deleted = models.BooleanField(default=False, verbose_name=_("Is deleted"))

    def __str__(self):
        return f"Place({self.osm_id})"

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
        ordering = ["-id"]
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
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    deleted = models.BooleanField(default=False, verbose_name=_("Is deleted"))

    def __str__(self):
        return f"PlaceA({self.osm_id})"

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
        ordering = ["-id"]
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
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    deleted = models.BooleanField(default=False, verbose_name=_("Is deleted"))

    def __str__(self):
        return f"Pofw({self.osm_id})"

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
        ordering = ["-id"]
        verbose_name = _("Pofw")
        verbose_name_plural = _("Pofw")
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
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    deleted = models.BooleanField(default=False, verbose_name=_("Is deleted"))

    def __str__(self):
        return f"PofwA({self.osm_id})"

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
        ordering = ["-id"]
        verbose_name = _("Pofw A")
        verbose_name_plural = _("Pofw A")
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
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    deleted = models.BooleanField(default=False, verbose_name=_("Is deleted"))

    def __str__(self):
        return f"Pois({self.osm_id})"

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
        ordering = ["-id"]
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
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    deleted = models.BooleanField(default=False, verbose_name=_("Is deleted"))

    def __str__(self):
        return f"PoisA({self.osm_id})"

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
        ordering = ["-id"]
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
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    deleted = models.BooleanField(default=False, verbose_name=_("Is deleted"))

    def __str__(self):
        return f"RailWay({self.osm_id})"

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
        ordering = ["-id"]
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
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    deleted = models.BooleanField(default=False, verbose_name=_("Is deleted"))

    def __str__(self):
        return f"Road({self.osm_id})"

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
        ordering = ["-id"]
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
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    deleted = models.BooleanField(default=False, verbose_name=_("Is deleted"))

    def __str__(self):
        return f"Traffic({self.osm_id})"

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
        ordering = ["-id"]
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
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    deleted = models.BooleanField(default=False, verbose_name=_("Is deleted"))

    def __str__(self):
        return f"TrafficA({self.osm_id})"

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
        ordering = ["-id"]
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
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    deleted = models.BooleanField(default=False, verbose_name=_("Is deleted"))

    def __str__(self):
        return f"Transport({self.osm_id})"

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
        ordering = ["-id"]
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
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    deleted = models.BooleanField(default=False, verbose_name=_("Is deleted"))

    def __str__(self):
        return f"TransportA({self.osm_id})"

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
        ordering = ["-id"]
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
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    deleted = models.BooleanField(default=False, verbose_name=_("Is deleted"))

    def __str__(self):
        return f"Water({self.osm_id})"

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
        ordering = ["-id"]
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
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    deleted = models.BooleanField(default=False, verbose_name=_("Is deleted"))

    def __str__(self):
        return f"WaterWay({self.osm_id})"

    @staticmethod
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
        ordering = ["-id"]
        verbose_name = _("Water Way")
        verbose_name_plural = _("WaterWays")
        app_label = "osm"
