# -*- coding: utf-8 -*-
from django.contrib.gis import admin

from osm import models


@admin.register(models.Building)
class BuildingAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "type"]
    list_filter = ["type"]


@admin.register(models.Landuse)
class LanduseAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name"]


@admin.register(models.Natural)
class NaturalAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name"]


@admin.register(models.NaturalA)
class NaturalA_Admin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name"]


@admin.register(models.Place)
class PlaceAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name"]


@admin.register(models.PlaceA)
class PlaceA_Admin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name"]


@admin.register(models.PofwA)
class PofwA_Admin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name"]


@admin.register(models.Pois)
class PoisAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "fclass"]


@admin.register(models.PoisA)
class PoisA_Admin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "fclass"]


@admin.register(models.RailWay)
class RailWayAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "fclass"]


@admin.register(models.Road)
class RoadAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "fclass", "maxspeed"]


@admin.register(models.Traffic)
class TrafficAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "fclass"]


@admin.register(models.TrafficA)
class TrafficA_Admin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "fclass"]


@admin.register(models.Transport)
class TransportAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "fclass"]


@admin.register(models.TransportA)
class TransportA_Admin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "fclass"]


@admin.register(models.Water)
class WaterAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "fclass"]


@admin.register(models.WaterWay)
class WaterWayAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "fclass"]

