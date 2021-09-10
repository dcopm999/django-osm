#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-osm
------------

Tests for `django-osm` models module.
"""

from django.test import TestCase

from osm import models


class CountryCase(TestCase):
    databases = "__all__"
    fixtures = ["osm"]

    def setUp(self):
        self.mapping = {
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

    def test_mapping(self):
        self.assertEqual(models.Country.mapping(), self.mapping)

    def test_str_(self):
        row = models.Country.objects.last()
        self.assertEqual(row.__str__(), f"Country({row.name})")


class BuildingCase(TestCase):
    databases = "__all__"
    fixtures = ["osm"]

    def setUp(self):
        self.mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "type": "type",
            "geom": "POLYGON",
        }

    def test_mapping(self):
        self.assertEqual(models.Building.mapping(), self.mapping)

    def test_str_(self):
        row = models.Building.objects.last()
        self.assertEqual(row.__str__(), f"Building({row.osm_id})")


class LanduseCase(TestCase):
    databases = "__all__"
    fixtures = ["osm"]

    def setUp(self):
        self.mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }

    def test_mapping(self):
        self.assertEqual(models.Landuse.mapping(), self.mapping)

    def test_str_(self):
        row = models.Landuse.objects.last()
        self.assertEqual(row.__str__(), f"Landuse({row.osm_id})")


class NaturalCase(TestCase):
    databases = "__all__"
    fixtures = ["osm"]

    def setUp(self):
        self.mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "POINT",
        }

    def test_mapping(self):
        self.assertEqual(models.Natural.mapping(), self.mapping)

    def test_str_(self):
        row = models.Natural.objects.last()
        self.assertEqual(row.__str__(), f"Natural({row.osm_id})")


class NaturalACase(TestCase):
    databases = "__all__"
    fixtures = ["osm"]

    def setUp(self):
        self.mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }

    def test_mapping(self):
        self.assertEqual(models.NaturalA.mapping(), self.mapping)

    def test_str_(self):
        row = models.NaturalA.objects.last()
        self.assertEqual(row.__str__(), f"NaturalA({row.osm_id})")


class PlaceCase(TestCase):
    databases = "__all__"
    fixtures = ["osm"]

    def setUp(self):
        self.mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "population": "population",
            "name": "name",
            "geom": "MULTIPOINT",
        }

    def test_mapping(self):
        self.assertEqual(models.Place.mapping(), self.mapping)

    def test_str_(self):
        row = models.Place.objects.last()
        self.assertEqual(row.__str__(), f"Place({row.osm_id})")


class PlaceACase(TestCase):
    databases = "__all__"
    fixtures = ["osm"]

    def setUp(self):
        self.mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "population": "population",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }

    def test_mapping(self):
        self.assertEqual(models.PlaceA.mapping(), self.mapping)

    def test_str_(self):
        row = models.PlaceA.objects.last()
        self.assertEqual(row.__str__(), f"PlaceA({row.osm_id})")


class PofwCase(TestCase):
    databases = "__all__"
    fixtures = ["osm"]

    def setUp(self):
        self.mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOINT",
        }

    def test_mapping(self):
        self.assertEqual(models.Pofw.mapping(), self.mapping)

    def test_str_(self):
        row = models.Pofw.objects.last()
        self.assertEqual(row.__str__(), f"Pofw({row.osm_id})")


class PofwACase(TestCase):
    databases = "__all__"
    fixtures = ["osm"]

    def setUp(self):
        self.mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }

    def test_mapping(self):
        self.assertEqual(models.PofwA.mapping(), self.mapping)

    def test_str_(self):
        row = models.PofwA.objects.last()
        self.assertEqual(row.__str__(), f"PofwA({row.osm_id})")


class PoisCase(TestCase):
    databases = "__all__"
    fixtures = ["osm"]

    def setUp(self):
        self.mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "POINT",
        }

    def test_mapping(self):
        self.assertEqual(models.Pois.mapping(), self.mapping)

    def test_str_(self):
        row = models.Pois.objects.last()
        self.assertEqual(row.__str__(), f"Pois({row.osm_id})")


class PoisACase(TestCase):
    databases = "__all__"
    fixtures = ["osm"]

    def setUp(self):
        self.mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }

    def test_mapping(self):
        self.assertEqual(models.PoisA.mapping(), self.mapping)

    def test_str_(self):
        row = models.PoisA.objects.last()
        self.assertEqual(row.__str__(), f"PoisA({row.osm_id})")


class RailWayCase(TestCase):
    databases = "__all__"
    fixtures = ["osm"]

    def setUp(self):
        self.mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "layer": "layer",
            "bridge": "bridge",
            "tunnel": "tunnel",
            "geom": "MULTILINESTRING",
        }

    def test_mapping(self):
        self.assertEqual(models.RailWay.mapping(), self.mapping)

    def test_str_(self):
        row = models.RailWay.objects.last()
        self.assertEqual(row.__str__(), f"RailWay({row.osm_id})")


class RoadCase(TestCase):
    databases = "__all__"
    fixtures = ["osm"]

    def setUp(self):
        self.mapping = {
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

    def test_mapping(self):
        self.assertEqual(models.Road.mapping(), self.mapping)

    def test_str_(self):
        row = models.Road.objects.last()
        self.assertEqual(row.__str__(), f"Road({row.osm_id})")


class TrafficCase(TestCase):
    databases = "__all__"
    fixtures = ["osm"]

    def setUp(self):
        self.mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOINT",
        }

    def test_mapping(self):
        self.assertEqual(models.Traffic.mapping(), self.mapping)

    def test_str_(self):
        row = models.Traffic.objects.last()
        self.assertEqual(row.__str__(), f"Traffic({row.osm_id})")


class TrafficACase(TestCase):
    databases = "__all__"
    fixtures = ["osm"]

    def setUp(self):
        self.mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }

    def test_mapping(self):
        self.assertEqual(models.TrafficA.mapping(), self.mapping)

    def test_str_(self):
        row = models.TrafficA.objects.last()
        self.assertEqual(row.__str__(), f"TrafficA({row.osm_id})")


class TransportCase(TestCase):
    databases = "__all__"
    fixtures = ["osm"]

    def setUp(self):
        self.mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOINT",
        }

    def test_mapping(self):
        self.assertEqual(models.Transport.mapping(), self.mapping)

    def test_str_(self):
        row = models.Transport.objects.last()
        self.assertEqual(row.__str__(), f"Transport({row.osm_id})")


class TransportACase(TestCase):
    databases = "__all__"
    fixtures = ["osm"]

    def setUp(self):
        self.mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }

    def test_mapping(self):
        self.assertEqual(models.TransportA.mapping(), self.mapping)

    def test_str_(self):
        row = models.TransportA.objects.last()
        self.assertEqual(row.__str__(), f"TransportA({row.osm_id})")


class WaterCase(TestCase):
    databases = "__all__"
    fixtures = ["osm"]

    def setUp(self):
        self.mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }

    def test_mapping(self):
        self.assertEqual(models.Water.mapping(), self.mapping)

    def test_str_(self):
        row = models.Water.objects.last()
        self.assertEqual(row.__str__(), f"Water({row.osm_id})")


class WaterWayCase(TestCase):
    databases = "__all__"
    fixtures = ["osm"]

    def setUp(self):
        self.mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "width": "width",
            "name": "name",
            "geom": "MULTILINESTRING",
        }

    def test_mapping(self):
        self.assertEqual(models.WaterWay.mapping(), self.mapping)

    def test_str_(self):
        row = models.WaterWay.objects.last()
        self.assertEqual(row.__str__(), f"WaterWay({row.osm_id})")
