=====
Usage
=====

To use django-osm in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'osm.apps.OsmConfig',
        ...
    )

Add django-osm's URL patterns:

.. code-block:: python

    from osm import urls as osm_urls


    urlpatterns = [
        ...
        url(r'^', include(osm_urls)),
        ...
    ]
