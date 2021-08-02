import logging
import os
import zipfile

import wget
from django.conf import settings
from django.core.management.base import BaseCommand

from osm import tasks

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Import OSM poligons"
    GDAL_DIR = os.path.join(settings.STATIC_ROOT, "gdal")
    URL_UZBEKISTAN = "https://download.geofabrik.de/asia/uzbekistan-latest-free.shp.zip"
    OSM_DIR = os.path.join(GDAL_DIR, "osm")

    def add_arguments(self, parser):
        parser.add_argument(
            "--Uzbekistan",
            action="store_true",
            default=False,
            help="Download and loading from OSM Server for Tashkent city",
        )
        parser.add_argument(
            "--URL",
            action="store_true",
            default=False,
            help="Download and loading from URL",
        )

    def handle(self, *args, **options):
        if not os.path.isdir(self.OSM_DIR):
            os.makedirs(self.OSM_DIR)
        if options["Uzbekistan"]:
            self.load_osm(self.URL_UZBEKISTAN)
        else:
            self.load_osm(options["URL"])

    def load_osm(self, url: str):
        file_name = self.URL_UZBEKISTAN.split("/")[-1]
        self.downloader(self.URL_UZBEKISTAN, self.OSM_DIR)
        with zipfile.ZipFile(os.path.join(self.OSM_DIR, file_name)) as zip_file:
            zip_file.extractall(self.OSM_DIR)
        tasks.osm_import.delay(
            "Building", os.path.join(self.OSM_DIR, "gis_osm_buildings_a_free_1.shp")
        )
        tasks.osm_import.delay(
            "Landuse", os.path.join(self.OSM_DIR, "gis_osm_landuse_a_free_1.shp")
        )
        tasks.osm_import.delay(
            "Natural", os.path.join(self.OSM_DIR, "gis_osm_natural_free_1.shp")
        )
        tasks.osm_import.delay(
            "NaturalA", os.path.join(self.OSM_DIR, "gis_osm_natural_a_free_1.shp")
        )
        tasks.osm_import.delay(
            "Place", os.path.join(self.OSM_DIR, "gis_osm_places_free_1.shp")
        )
        tasks.osm_import.delay(
            "PlaceA", os.path.join(self.OSM_DIR, "gis_osm_places_a_free_1.shp")
        )
        tasks.osm_import.delay(
            "Pofw", os.path.join(self.OSM_DIR, "gis_osm_pofw_free_1.shp")
        )
        tasks.osm_import.delay(
            "PofwA", os.path.join(self.OSM_DIR, "gis_osm_pofw_a_free_1.shp")
        )
        tasks.osm_import.delay(
            "Pois", os.path.join(self.OSM_DIR, "gis_osm_pois_free_1.shp")
        )
        tasks.osm_import.delay(
            "PoisA", os.path.join(self.OSM_DIR, "gis_osm_pois_a_free_1.shp")
        )
        tasks.osm_import.delay(
            "RailWay", os.path.join(self.OSM_DIR, "gis_osm_railways_free_1.shp")
        )
        tasks.osm_import.delay(
            "Road", os.path.join(self.OSM_DIR, "gis_osm_roads_free_1.shp")
        )
        tasks.osm_import.delay(
            "Traffic", os.path.join(self.OSM_DIR, "gis_osm_traffic_free_1.shp")
        )
        tasks.osm_import.delay(
            "TrafficA", os.path.join(self.OSM_DIR, "gis_osm_traffic_a_free_1.shp")
        )
        tasks.osm_import.delay(
            "Transport", os.path.join(self.OSM_DIR, "gis_osm_transport_free_1.shp")
        )
        tasks.osm_import.delay(
            "TransportA", os.path.join(self.OSM_DIR, "gis_osm_transport_a_free_1.shp")
        )
        tasks.osm_import.delay(
            "Water", os.path.join(self.OSM_DIR, "gis_osm_water_a_free_1.shp")
        )
        tasks.osm_import.delay(
            "WaterWay", os.path.join(self.OSM_DIR, "gis_osm_waterways_free_1.shp")
        )

    def downloader(self, url, path):
        self.stdout.write(f"Downloading file: {self.URL_UZBEKISTAN}")
        wget.download(url, path)
        self.stdout.write(self.style.SUCCESS("\tSuccess"))
