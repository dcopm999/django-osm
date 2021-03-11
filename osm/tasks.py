import os

from celery import shared_task
from django.conf import settings
from django.contrib.gis.utils import LayerMapping

from osm import models


# @celery_app.task(bind=True)
@shared_task
def osm_import(osm_model, osm_filename, verbose=True):
    osm_model = getattr(models, osm_model)
    lm = LayerMapping(
        osm_model,
        osm_filename,
        osm_model.mapping(),
        transform=False,
        transaction_mode="autocommit",
        unique="osm_id",
    )
    lm.save(strict=True, verbose=verbose)


@shared_task
def world_osm_import(verbose=True):
    osm_model = models.World
    osm_filename = os.path.join(
        settings.STATIC_ROOT, "gdal", "world", "TM_WORLD_BORDERS-0.3.shp"
    )
    lm = LayerMapping(
        osm_model,
        osm_filename,
        osm_model.mapping(),
        transform=False,
        transaction_mode="autocommit",
        unique="name",
    )
    lm.save(strict=True, verbose=verbose)
