# Generated by Django 3.1.5 on 2021-01-20 11:18

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
            ],
            options={
                'verbose_name': 'Building',
                'verbose_name_plural': 'Buildings',
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
            ],
            options={
                'verbose_name': 'Landuse',
                'verbose_name_plural': 'Landuses',
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
            ],
            options={
                'verbose_name': 'Natural',
                'verbose_name_plural': 'Naturals',
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
            ],
            options={
                'verbose_name': 'Natural A',
                'verbose_name_plural': 'Naturals A',
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
            ],
            options={
                'verbose_name': 'Place',
                'verbose_name_plural': 'Places',
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
            ],
            options={
                'verbose_name': 'Place A',
                'verbose_name_plural': 'Places A',
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
            ],
            options={
                'verbose_name': 'Pofw',
                'verbose_name_plural': 'Pofws',
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
            ],
            options={
                'verbose_name': 'Pofw A',
                'verbose_name_plural': 'Pofws A',
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
            ],
            options={
                'verbose_name': 'Pois',
                'verbose_name_plural': 'Poises',
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
            ],
            options={
                'verbose_name': 'Pois A',
                'verbose_name_plural': 'Poises A',
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
            ],
            options={
                'verbose_name': 'RailWay',
                'verbose_name_plural': 'RailWays',
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
            ],
            options={
                'verbose_name': 'Road',
                'verbose_name_plural': 'Roads',
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
            ],
            options={
                'verbose_name': 'Traffic',
                'verbose_name_plural': 'Traffics',
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
            ],
            options={
                'verbose_name': 'Traffic A',
                'verbose_name_plural': 'Traffics A',
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
            ],
            options={
                'verbose_name': 'Transport',
                'verbose_name_plural': 'Transports',
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
            ],
            options={
                'verbose_name': 'Transport A',
                'verbose_name_plural': 'Transports A',
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
            ],
            options={
                'verbose_name': 'Water',
                'verbose_name_plural': 'Waters',
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
            ],
        ),
    ]
