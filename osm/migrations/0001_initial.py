# Generated by Django 3.2.5 on 2021-08-02 05:23

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osm_id', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='OSM ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('fclass', models.CharField(max_length=28, verbose_name='Object class')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('type', models.CharField(blank=True, max_length=20, null=True, verbose_name='Object Type')),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
            ],
            options={
                'verbose_name': 'Building',
                'verbose_name_plural': 'Buildings',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fips', models.CharField(blank=True, max_length=2, null=True, verbose_name='Fips')),
                ('iso2', models.CharField(max_length=2, verbose_name='iso2')),
                ('iso3', models.CharField(max_length=3, verbose_name='iso3')),
                ('un', models.IntegerField(verbose_name='UN')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Name')),
                ('area', models.IntegerField(verbose_name='Area')),
                ('pop2005', models.BigIntegerField(verbose_name='Pop 2005')),
                ('region', models.IntegerField(verbose_name='Region')),
                ('subregion', models.IntegerField(verbose_name='Subregion')),
                ('lon', models.FloatField(verbose_name='Lon')),
                ('lat', models.FloatField(verbose_name='Lat')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, verbose_name='Geom')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Landuse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osm_id', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='OSM ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('fclass', models.CharField(max_length=28, verbose_name='Object class')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
            ],
            options={
                'verbose_name': 'Landuse',
                'verbose_name_plural': 'Landuses',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Natural',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osm_id', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='OSM ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('fclass', models.CharField(max_length=28, verbose_name='Object class')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
            ],
            options={
                'verbose_name': 'Natural',
                'verbose_name_plural': 'Naturals',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='NaturalA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osm_id', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='OSM ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('fclass', models.CharField(max_length=28, verbose_name='Object class')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
            ],
            options={
                'verbose_name': 'Natural A',
                'verbose_name_plural': 'Naturals A',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osm_id', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='OSM ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('fclass', models.CharField(max_length=28, verbose_name='Object class')),
                ('population', models.BigIntegerField()),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
            ],
            options={
                'verbose_name': 'Place',
                'verbose_name_plural': 'Places',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PlaceA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osm_id', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='OSM ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('fclass', models.CharField(max_length=28, verbose_name='Object class')),
                ('population', models.BigIntegerField()),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
            ],
            options={
                'verbose_name': 'Place A',
                'verbose_name_plural': 'Places A',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Pofw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osm_id', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='OSM ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('fclass', models.CharField(max_length=28, verbose_name='Object class')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
            ],
            options={
                'verbose_name': 'Pofw',
                'verbose_name_plural': 'Pofw',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PofwA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osm_id', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='OSM ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('fclass', models.CharField(max_length=28, verbose_name='Object class')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
            ],
            options={
                'verbose_name': 'Pofw A',
                'verbose_name_plural': 'Pofw A',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Pois',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osm_id', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='OSM ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('fclass', models.CharField(max_length=28, verbose_name='Object class')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
            ],
            options={
                'verbose_name': 'Pois',
                'verbose_name_plural': 'Poises',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PoisA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osm_id', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='OSM ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('fclass', models.CharField(max_length=28, verbose_name='Object class')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
            ],
            options={
                'verbose_name': 'Pois A',
                'verbose_name_plural': 'Poises A',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='RailWay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osm_id', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='OSM ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('fclass', models.CharField(max_length=28, verbose_name='Object class')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('layer', models.BigIntegerField(verbose_name='Layer')),
                ('bridge', models.CharField(max_length=1, verbose_name='Bridge')),
                ('tunnel', models.CharField(max_length=1, verbose_name='Tunnel')),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
            ],
            options={
                'verbose_name': 'RailWay',
                'verbose_name_plural': 'RailWays',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Road',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osm_id', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='OSM ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('fclass', models.CharField(max_length=28, verbose_name='Object class')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Object name')),
                ('ref', models.CharField(max_length=20, null=True, verbose_name='Ref')),
                ('oneway', models.CharField(max_length=1, verbose_name='One way')),
                ('maxspeed', models.IntegerField(verbose_name='Max speed')),
                ('layer', models.BigIntegerField(verbose_name='Layer')),
                ('bridge', models.CharField(max_length=1, verbose_name='Bridge')),
                ('tunnel', models.CharField(max_length=1, verbose_name='Tunnel')),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
            ],
            options={
                'verbose_name': 'Road',
                'verbose_name_plural': 'Roads',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Traffic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osm_id', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='OSM ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('fclass', models.CharField(max_length=28, verbose_name='Object class')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Object name')),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
            ],
            options={
                'verbose_name': 'Traffic',
                'verbose_name_plural': 'Traffics',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='TrafficA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osm_id', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='OSM ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('fclass', models.CharField(max_length=28, verbose_name='Object class')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Object name')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
            ],
            options={
                'verbose_name': 'Traffic A',
                'verbose_name_plural': 'Traffics A',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osm_id', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='OSM ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('fclass', models.CharField(max_length=28, verbose_name='Object class')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Object name')),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
            ],
            options={
                'verbose_name': 'Transport',
                'verbose_name_plural': 'Transports',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='TransportA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osm_id', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='OSM ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('fclass', models.CharField(max_length=28, verbose_name='Object class')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Object name')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
            ],
            options={
                'verbose_name': 'Transport A',
                'verbose_name_plural': 'Transports A',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Water',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osm_id', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='OSM ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('fclass', models.CharField(max_length=28, verbose_name='Object class')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Object name')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
            ],
            options={
                'verbose_name': 'Water',
                'verbose_name_plural': 'Waters',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='WaterWay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osm_id', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='OSM ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('fclass', models.CharField(max_length=28, verbose_name='Object class')),
                ('width', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Object name')),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
            ],
            options={
                'verbose_name': 'Water Way',
                'verbose_name_plural': 'WaterWays',
                'ordering': ['-id'],
            },
        ),
    ]
