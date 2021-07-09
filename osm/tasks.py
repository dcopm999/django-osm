import os

from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings
from django.contrib.gis.utils import LayerMapping

from osm import models

logger = get_task_logger(__name__)


@shared_task(bind=True, ignore_results=True)
def osm_import(self, osm_model, osm_filename, verbose=True):
    osm_model = getattr(models, osm_model)
    lm = LayerMapping(
        osm_model,
        osm_filename,
        osm_model.mapping(),
        transform=True,
        transaction_mode="autocommit",
        unique="osm_id",
    )
    lm.save(strict=True, verbose=verbose)


@shared_task(bind=True, ignore_results=True)
def osm_world_import(self, verbose=True):
    osm_model = models.World
    osm_filename = os.path.join(
        settings.STATIC_ROOT, "gdal", "world", "TM_WORLD_BORDERS-0.3.shp"
    )
    lm = LayerMapping(
        osm_model,
        osm_filename,
        osm_model.mapping(),
        transform=True,
        transaction_mode="autocommit",
        unique="name",
    )
    lm.save(strict=True, verbose=verbose)
