from django.contrib.gis.utils import LayerMapping
from celery import shared_task

from osm import models


#@celery_app.task(bind=True)
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
