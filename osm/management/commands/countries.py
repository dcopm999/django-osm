import logging
import os
import zipfile

import wget
from django.conf import settings
from django.core.management.base import BaseCommand

from osm import tasks

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "OSM countries poligons import"
    GDAL_DIR = os.path.join(settings.STATIC_ROOT, "gdal")
    URL_COUNTRIES = "https://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip"
    OSM_DIR = os.path.join(GDAL_DIR, "countries")

    def handle(self, *args, **options):
        if not os.path.isdir(self.OSM_DIR):
            os.makedirs(self.OSM_DIR)

        file_name = self.URL_COUNTRIES.split("/")[-1]
        self.downloader(self.URL_COUNTRIES, self.OSM_DIR)
        with zipfile.ZipFile(os.path.join(self.OSM_DIR, file_name)) as zip_file:
            zip_file.extractall(self.OSM_DIR)
        tasks.osm_country_import.delay()

    def downloader(self, url, path):
        self.stdout.write(f"Downloading file: {self.URL_COUNTRIES}")
        wget.download(url, path)
        self.stdout.write(self.style.SUCCESS("\tSuccess"))
