#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-osm
------------

Tests for `django-osm` route_db module.
"""
from django.conf import settings
from django.contrib.gis.db.models import Model
from django.test import TestCase

from osm import models
from osm.route_db import Default


class OTHER_MODEL(Model):
    class Meta:
        app_label = "qwerty"


class RouteCase(TestCase):
    ROUTER = Default()

    def test_db_form_read_osm(self):
        self.assertEqual(
            self.ROUTER.db_for_read(models.Country), settings.OSM_REPLICS[0]
        )

    def test_db_form_read_other(self):
        self.assertEqual(self.ROUTER.db_for_read(OTHER_MODEL), None)

    def test_db_form_write_osm(self):
        self.assertEqual(self.ROUTER.db_for_write(models.Country), "osm")

    def test_db_form_write_other(self):
        self.assertEqual(self.ROUTER.db_for_write(OTHER_MODEL), None)

    def test_allow_relation_true(self):
        self.assertTrue(self.ROUTER.allow_relation(models.Country, models.Building))

    def test_allow_relation_false(self):
        self.assertEqual(self.ROUTER.allow_relation(OTHER_MODEL, OTHER_MODEL), None)
