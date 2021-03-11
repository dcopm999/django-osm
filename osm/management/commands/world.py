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
    URL_WORLD = "https://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip"

    def handle(self, *args, **options):
        if not os.path.isdir(self.GDAL_DIR):
            os.mkdir(self.GDAL_DIR)
        self.load_world()

    def load_world(self):
        osm_dir = os.path.join(self.GDAL_DIR, "world")
        file_name = self.URL_WORLD.split("/")[-1]
        if not os.path.isdir(osm_dir):
            os.mkdir(osm_dir)
        self.downloader(self.URL_WORLD, osm_dir)
        with zipfile.ZipFile(os.path.join(osm_dir, file_name)) as zip_file:
            zip_file.extractall(osm_dir)

        tasks.world_osm_import.delay()

    def downloader(self, url, path):
        self.stdout.write(f"Downloading file: {self.URL_WORLD}")
        wget.download(url, path)
        self.stdout.write(self.style.SUCCESS("\tSuccess"))
