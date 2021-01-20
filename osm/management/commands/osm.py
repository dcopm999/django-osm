import logging
import os
import zipfile

import wget
from django.conf import settings
from django.core.management.base import BaseCommand

from osm import tasks

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "OSM import"
    GDAL_DIR = os.path.join(settings.STATIC_ROOT, "gdal")
    URL_UZBEKISTAN = "https://download.geofabrik.de/asia/uzbekistan-latest-free.shp.zip"

    def add_arguments(self, parser):
        parser.add_argument(
            "--Uzbekistan",
            action="store_true",
            default=False,
            help="Download and loading from OSM Server for Tashkent city",
        )

    def handle(self, *args, **options):
        if not os.path.isdir(self.GDAL_DIR):
            os.mkdir(self.GDAL_DIR)
        if options["Uzbekistan"]:
            self.load_uzbekistan()

    def load_uzbekistan(self):
        osm_dir = os.path.join(self.GDAL_DIR, "Uzbekistan")
        file_name = self.URL_UZBEKISTAN.split("/")[-1]
        if not os.path.isdir(osm_dir):
            os.mkdir(osm_dir)
        self.downloader(self.URL_UZBEKISTAN, osm_dir)
        with zipfile.ZipFile(os.path.join(osm_dir, file_name)) as zip_file:
            zip_file.extractall(osm_dir)
        tasks.osm_import.delay(
            "Building", os.path.join(osm_dir, "gis_osm_buildings_a_free_1.shp")
        )
        tasks.osm_import.delay(
            "Landuse", os.path.join(osm_dir, "gis_osm_landuse_a_free_1.shp")
        )
        tasks.osm_import.delay(
            "Natural", os.path.join(osm_dir, "gis_osm_natural_free_1.shp")
        )
        tasks.osm_import.delay(
            "NaturalA", os.path.join(osm_dir, "gis_osm_natural_a_free_1.shp")
        )
        tasks.osm_import.delay(
            "Place", os.path.join(osm_dir, "gis_osm_places_free_1.shp")
        )
        tasks.osm_import.delay(
            "PlaceA", os.path.join(osm_dir, "gis_osm_places_a_free_1.shp")
        )
        tasks.osm_import.delay("Pofw", os.path.join(osm_dir, "gis_osm_pofw_free_1.shp"))
        tasks.osm_import.delay(
            "PofwA", os.path.join(osm_dir, "gis_osm_pofw_a_free_1.shp")
        )
        tasks.osm_import.delay("Pois", os.path.join(osm_dir, "gis_osm_pois_free_1.shp"))
        tasks.osm_import.delay(
            "PoisA", os.path.join(osm_dir, "gis_osm_pois_a_free_1.shp")
        )
        tasks.osm_import.delay(
            "RailWay", os.path.join(osm_dir, "gis_osm_railways_free_1.shp")
        )
        tasks.osm_import.delay(
            "Road", os.path.join(osm_dir, "gis_osm_roads_free_1.shp")
        )
        tasks.osm_import.delay(
            "Traffic", os.path.join(osm_dir, "gis_osm_traffic_free_1.shp")
        )
        tasks.osm_import.delay(
            "TrafficA", os.path.join(osm_dir, "gis_osm_traffic_a_free_1.shp")
        )
        tasks.osm_import.delay(
            "Transport", os.path.join(osm_dir, "gis_osm_transport_free_1.shp")
        )
        tasks.osm_import.delay(
            "TransportA", os.path.join(osm_dir, "gis_osm_transport_a_free_1.shp")
        )
        tasks.osm_import.delay(
            "Water", os.path.join(osm_dir, "gis_osm_water_a_free_1.shp")
        )
        tasks.osm_import.delay(
            "WaterWay", os.path.join(osm_dir, "gis_osm_waterways_free_1.shp")
        )

    def downloader(self, url, path):
        self.stdout.write(f"Downloading file: {self.URL_UZBEKISTAN}")
        wget.download(url, path)
        self.stdout.write(self.style.SUCCESS("\tSuccess"))
