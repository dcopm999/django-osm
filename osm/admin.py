# -*- coding: utf-8 -*-
from django.contrib.gis import admin

from osm import models


@admin.register(models.Country)
class CountryAdmin(admin.OSMGeoAdmin):
    list_display = [
        "name",
        "fips",
        "iso2",
        "iso3",
        "un",
        "area",
        "pop2005",
        "created",
        "updated",
        "deleted",
    ]
    search_fields = ["name"]
    date_hierarchy = "updated"
    list_editable = ["deleted"]


@admin.register(models.Building)
class BuildingAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "code", "fclass", "created", "updated", "deleted"]
    list_filter = ["fclass"]
    search_fields = ["name", "osm_id"]
    date_hierarchy = "updated"
    list_editable = ["deleted"]


@admin.register(models.Landuse)
class LanduseAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "code", "fclass", "created", "updated", "deleted"]
    list_filter = ["fclass"]
    search_fields = ["name", "osm_id"]
    date_hierarchy = "updated"
    list_editable = ["deleted"]


@admin.register(models.Natural)
class NaturalAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "code", "fclass", "created", "updated", "deleted"]
    list_filter = ["fclass"]
    search_fields = ["name", "osm_id"]
    date_hierarchy = "updated"
    list_editable = ["deleted"]


@admin.register(models.NaturalA)
class NaturalA_Admin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "code", "fclass", "created", "updated", "deleted"]
    list_filter = ["fclass"]
    search_fields = ["name", "osm_id"]
    date_hierarchy = "updated"
    list_editable = ["deleted"]


@admin.register(models.Place)
class PlaceAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "code", "fclass", "created", "updated", "deleted"]
    list_filter = ["fclass"]
    search_fields = ["name", "osm_id"]
    date_hierarchy = "updated"
    list_editable = ["deleted"]


@admin.register(models.PlaceA)
class PlaceA_Admin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "code", "fclass", "created", "updated", "deleted"]
    list_filter = ["fclass"]
    search_fields = ["name", "osm_id"]
    list_filter = ["fclass"]
    date_hierarchy = "updated"
    list_editable = ["deleted"]


@admin.register(models.Pofw)
class PofwAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "code", "fclass", "created", "updated", "deleted"]
    list_filter = ["fclass"]
    search_fields = ["name", "osm_id"]
    date_hierarchy = "updated"
    list_editable = ["deleted"]


@admin.register(models.PofwA)
class PofwA_Admin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "code", "fclass", "created", "updated", "deleted"]
    list_filter = ["fclass"]
    search_fields = ["name", "osm_id"]
    date_hierarchy = "updated"
    list_editable = ["deleted"]


@admin.register(models.Pois)
class PoisAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "code", "fclass", "created", "updated", "deleted"]
    list_filter = ["fclass"]
    search_fields = ["name", "osm_id"]
    date_hierarchy = "updated"
    list_editable = ["deleted"]


@admin.register(models.PoisA)
class PoisA_Admin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "code", "fclass", "created", "updated", "deleted"]
    list_filter = ["fclass"]
    search_fields = ["name", "osm_id"]
    date_hierarchy = "updated"
    list_editable = ["deleted"]


@admin.register(models.RailWay)
class RailWayAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "code", "fclass", "created", "updated", "deleted"]
    list_filter = ["fclass"]
    search_fields = ["name", "osm_id"]
    date_hierarchy = "updated"
    list_editable = ["deleted"]


@admin.register(models.Road)
class RoadAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "code", "fclass", "created", "updated", "deleted"]
    list_filter = ["fclass"]
    search_fields = ["name", "osm_id"]
    date_hierarchy = "updated"
    list_editable = ["deleted"]


@admin.register(models.Traffic)
class TrafficAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "code", "fclass", "created", "updated", "deleted"]
    list_filter = ["fclass"]
    search_fields = ["name", "osm_id"]
    date_hierarchy = "updated"
    list_editable = ["deleted"]


@admin.register(models.TrafficA)
class TrafficA_Admin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "code", "fclass", "created", "updated", "deleted"]
    list_filter = ["fclass"]
    search_fields = ["name", "osm_id"]
    date_hierarchy = "updated"
    list_editable = ["deleted"]


@admin.register(models.Transport)
class TransportAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "code", "fclass", "created", "updated", "deleted"]
    list_filter = ["fclass"]
    search_fields = ["name", "osm_id"]
    date_hierarchy = "updated"
    list_editable = ["deleted"]


@admin.register(models.TransportA)
class TransportA_Admin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "code", "fclass", "created", "updated", "deleted"]
    list_filter = ["fclass"]
    search_fields = ["name", "osm_id"]
    date_hierarchy = "updated"
    list_editable = ["deleted"]


@admin.register(models.Water)
class WaterAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "code", "fclass", "created", "updated", "deleted"]
    list_filter = ["fclass"]
    search_fields = ["name", "osm_id"]
    date_hierarchy = "updated"
    list_editable = ["deleted"]


@admin.register(models.WaterWay)
class WaterWayAdmin(admin.OSMGeoAdmin):
    list_display = ["osm_id", "name", "code", "fclass", "created", "updated", "deleted"]
    list_filter = ["fclass"]
    search_fields = ["name", "osm_id"]
    date_hierarchy = "updated"
    list_editable = ["deleted"]
