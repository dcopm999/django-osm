=====
Usage
=====

To use django-osm in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
	"django.contrib.gis",
	"django_celery_beat",
	"rest_framework",
	"rest_framework_gis",
        "osm",
        ...
    )

    DATABASE_ROUTERS = [
        ...
        'osm.route_db.Default'
    ]

    DATABASES = {
        ...
        'osm': {
	    'ENGINE': 'django.contrib.gis.db.backends.postgis',
	    'HOST': 'localhost',
	    'NAME': 'geodjango',
	},
    }
    OSM_REPLICS = ['osm']


Add django-osm's URL patterns:

.. code-block:: python

    urlpatterns = [
        ...
	path('osm/', include('osm.urls', namespace='osm')),
        ...
    ]
