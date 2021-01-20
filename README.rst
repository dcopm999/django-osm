=============================
django-osm
=============================

.. image:: https://badge.fury.io/py/django-osm.svg
    :target: https://badge.fury.io/py/django-osm

.. image:: https://travis-ci.org/dcopm999/django-osm.svg?branch=master
    :target: https://travis-ci.org/dcopm999/django-osm

.. image:: https://codecov.io/gh/dcopm999/django-osm/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dcopm999/django-osm

Project Open Street Map management

Documentation
-------------

The full documentation is at https://django-osm.readthedocs.io.

Quickstart
----------

Install django-osm::

    pip install django-osm

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
	"django.contrib.gis",
	"django_celery_beat",
	"rest_framework",
	"rest_framework_gis",
	"django_elasticsearch_dsl",
	"django_elasticsearch_dsl_drf",
        "osm",
        ...
    )

    ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200'
	},
    }

    DATABASES = {
        'default': {
	'ENGINE': 'django.contrib.gis.db.backends.postgis',
	'NAME': 'geodjango',
	'USER': 'geo',
	},
    }


Add django-osm's URL patterns:

.. code-block:: python

    from osm import urls as osm_urls


    urlpatterns = [
        ...
        url(r'^', include(osm_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
