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

    def test_country_mapping(self):
        mapping = {
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
        self.assertEqual(models.Country.mapping(), mapping)

    def test_country_str_(self):
        row = models.Country.objects.last()
        self.assertEqual(row.__str__(), f"Country({row.name})")

    def test_building_mapping(self):
        mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "type": "type",
            "geom": "POLYGON",
        }
        self.assertEqual(models.Building.mapping(), mapping)

    def test_str_(self):
        row = models.Building.objects.last()
        self.assertEqual(row.__str__(), f"Building({row.osm_id})")

    def test_landuse_mapping(self):
        mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }
        self.assertEqual(models.Landuse.mapping(), mapping)

    def test_landuse_str_(self):
        row = models.Landuse.objects.last()
        self.assertEqual(row.__str__(), f"Landuse({row.osm_id})")

    def test_nuatural_mapping(self):
        mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "POINT",
        }
        self.assertEqual(models.Natural.mapping(), mapping)

    def test_natural_str_(self):
        row = models.Natural.objects.last()
        self.assertEqual(row.__str__(), f"Natural({row.osm_id})")

    def test_naturala_mapping(self):
        mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }
        self.assertEqual(models.NaturalA.mapping(), mapping)

    def test_naturala_str_(self):
        row = models.NaturalA.objects.last()
        self.assertEqual(row.__str__(), f"NaturalA({row.osm_id})")

    def test_place_mapping(self):
        mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "population": "population",
            "name": "name",
            "geom": "MULTIPOINT",
        }
        self.assertEqual(models.Place.mapping(), mapping)

    def test_place_str_(self):
        row = models.Place.objects.last()
        self.assertEqual(row.__str__(), f"Place({row.osm_id})")

    def test_placea_mapping(self):
        mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "population": "population",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }
        self.assertEqual(models.PlaceA.mapping(), mapping)

    def test_placea_str_(self):
        row = models.PlaceA.objects.last()
        self.assertEqual(row.__str__(), f"PlaceA({row.osm_id})")

    def test_pofw_mapping(self):
        mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOINT",
        }
        self.assertEqual(models.Pofw.mapping(), mapping)

    def test_pofw_str_(self):
        row = models.Pofw.objects.last()
        self.assertEqual(row.__str__(), f"Pofw({row.osm_id})")

    def test_pofwa_mapping(self):
        mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }

        self.assertEqual(models.PofwA.mapping(), mapping)

    def test_pofwa_str_(self):
        row = models.PofwA.objects.last()
        self.assertEqual(row.__str__(), f"PofwA({row.osm_id})")

    def test_pois_mapping(self):
        mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "POINT",
        }
        self.assertEqual(models.Pois.mapping(), mapping)

    def test_pois_str_(self):
        row = models.Pois.objects.last()
        self.assertEqual(row.__str__(), f"Pois({row.osm_id})")

    def test_poisa_mapping(self):
        mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }
        self.assertEqual(models.PoisA.mapping(), mapping)

    def test_poisa_str_(self):
        row = models.PoisA.objects.last()
        self.assertEqual(row.__str__(), f"PoisA({row.osm_id})")

    def test_railway_mapping(self):
        mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "layer": "layer",
            "bridge": "bridge",
            "tunnel": "tunnel",
            "geom": "MULTILINESTRING",
        }
        self.assertEqual(models.RailWay.mapping(), mapping)

    def test_railway_str_(self):
        row = models.RailWay.objects.last()
        self.assertEqual(row.__str__(), f"RailWay({row.osm_id})")

    def test_road_mapping(self):
        mapping = {
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
        self.assertEqual(models.Road.mapping(), mapping)

    def test_road_str_(self):
        row = models.Road.objects.last()
        self.assertEqual(row.__str__(), f"Road({row.osm_id})")

    def test_traffic_mapping(self):
        mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOINT",
        }
        self.assertEqual(models.Traffic.mapping(), mapping)

    def test_traffic_str_(self):
        row = models.Traffic.objects.last()
        self.assertEqual(row.__str__(), f"Traffic({row.osm_id})")

    def test_traffica_mapping(self):
        mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }
        self.assertEqual(models.TrafficA.mapping(), mapping)

    def test_traffica_str_(self):
        row = models.TrafficA.objects.last()
        self.assertEqual(row.__str__(), f"TrafficA({row.osm_id})")

    def test_transport_mapping(self):
        mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOINT",
        }
        self.assertEqual(models.Transport.mapping(), mapping)

    def test_transport_str_(self):
        row = models.Transport.objects.last()
        self.assertEqual(row.__str__(), f"Transport({row.osm_id})")

    def test_transporta_mapping(self):
        mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }
        self.assertEqual(models.TransportA.mapping(), mapping)

    def test_transporta_str_(self):
        row = models.TransportA.objects.last()
        self.assertEqual(row.__str__(), f"TransportA({row.osm_id})")

    def test_water_mapping(self):
        mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "name": "name",
            "geom": "MULTIPOLYGON",
        }
        self.assertEqual(models.Water.mapping(), mapping)

    def test_water_str_(self):
        row = models.Water.objects.last()
        self.assertEqual(row.__str__(), f"Water({row.osm_id})")

    def test_waterway_mapping(self):
        mapping = {
            "osm_id": "osm_id",
            "code": "code",
            "fclass": "fclass",
            "width": "width",
            "name": "name",
            "geom": "MULTILINESTRING",
        }
        self.assertEqual(models.WaterWay.mapping(), mapping)

    def test_waterway_str_(self):
        row = models.WaterWay.objects.last()
        self.assertEqual(row.__str__(), f"WaterWay({row.osm_id})")
