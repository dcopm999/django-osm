# Generated by Django 3.2.5 on 2022-05-31 07:08

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='building',
            options={'ordering': ['-osm_id'], 'verbose_name': 'Building', 'verbose_name_plural': 'Buildings'},
        ),
        migrations.AlterModelOptions(
            name='landuse',
            options={'ordering': ['-osm_id'], 'verbose_name': 'Landuse', 'verbose_name_plural': 'Landuses'},
        ),
        migrations.AlterModelOptions(
            name='natural',
            options={'ordering': ['-osm_id'], 'verbose_name': 'Natural', 'verbose_name_plural': 'Naturals'},
        ),
        migrations.AlterModelOptions(
            name='naturala',
            options={'ordering': ['-osm_id'], 'verbose_name': 'Natural A', 'verbose_name_plural': 'Naturals A'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['-osm_id'], 'verbose_name': 'Place', 'verbose_name_plural': 'Places'},
        ),
        migrations.AlterModelOptions(
            name='placea',
            options={'ordering': ['-osm_id'], 'verbose_name': 'Place A', 'verbose_name_plural': 'Places A'},
        ),
        migrations.AlterModelOptions(
            name='pofw',
            options={'ordering': ['-osm_id'], 'verbose_name': 'Pofw', 'verbose_name_plural': 'Pofw'},
        ),
        migrations.AlterModelOptions(
            name='pofwa',
            options={'ordering': ['-osm_id'], 'verbose_name': 'Pofw A', 'verbose_name_plural': 'Pofw A'},
        ),
        migrations.AlterModelOptions(
            name='pois',
            options={'ordering': ['-osm_id'], 'verbose_name': 'Pois', 'verbose_name_plural': 'Poises'},
        ),
        migrations.AlterModelOptions(
            name='poisa',
            options={'ordering': ['-osm_id'], 'verbose_name': 'Pois A', 'verbose_name_plural': 'Poises A'},
        ),
        migrations.AlterModelOptions(
            name='railway',
            options={'ordering': ['-osm_id'], 'verbose_name': 'RailWay', 'verbose_name_plural': 'RailWays'},
        ),
        migrations.AlterModelOptions(
            name='road',
            options={'ordering': ['-osm_id'], 'verbose_name': 'Road', 'verbose_name_plural': 'Roads'},
        ),
        migrations.AlterModelOptions(
            name='traffic',
            options={'ordering': ['-osm_id'], 'verbose_name': 'Traffic', 'verbose_name_plural': 'Traffics'},
        ),
        migrations.AlterModelOptions(
            name='traffica',
            options={'ordering': ['-osm_id'], 'verbose_name': 'Traffic A', 'verbose_name_plural': 'Traffics A'},
        ),
        migrations.AlterModelOptions(
            name='transport',
            options={'ordering': ['-osm_id'], 'verbose_name': 'Transport', 'verbose_name_plural': 'Transports'},
        ),
        migrations.AlterModelOptions(
            name='transporta',
            options={'ordering': ['-osm_id'], 'verbose_name': 'Transport A', 'verbose_name_plural': 'Transports A'},
        ),
        migrations.AlterModelOptions(
            name='water',
            options={'ordering': ['-osm_id'], 'verbose_name': 'Water', 'verbose_name_plural': 'Waters'},
        ),
        migrations.AlterModelOptions(
            name='waterway',
            options={'ordering': ['-osm_id'], 'verbose_name': 'Water Way', 'verbose_name_plural': 'WaterWays'},
        ),
        migrations.RemoveField(
            model_name='building',
            name='id',
        ),
        migrations.RemoveField(
            model_name='landuse',
            name='id',
        ),
        migrations.RemoveField(
            model_name='natural',
            name='id',
        ),
        migrations.RemoveField(
            model_name='naturala',
            name='id',
        ),
        migrations.RemoveField(
            model_name='place',
            name='id',
        ),
        migrations.RemoveField(
            model_name='placea',
            name='id',
        ),
        migrations.RemoveField(
            model_name='pofw',
            name='id',
        ),
        migrations.RemoveField(
            model_name='pofwa',
            name='id',
        ),
        migrations.RemoveField(
            model_name='pois',
            name='id',
        ),
        migrations.RemoveField(
            model_name='poisa',
            name='id',
        ),
        migrations.RemoveField(
            model_name='railway',
            name='id',
        ),
        migrations.RemoveField(
            model_name='road',
            name='id',
        ),
        migrations.RemoveField(
            model_name='traffic',
            name='id',
        ),
        migrations.RemoveField(
            model_name='traffica',
            name='id',
        ),
        migrations.RemoveField(
            model_name='transport',
            name='id',
        ),
        migrations.RemoveField(
            model_name='transporta',
            name='id',
        ),
        migrations.RemoveField(
            model_name='water',
            name='id',
        ),
        migrations.RemoveField(
            model_name='waterway',
            name='id',
        ),
        migrations.AlterField(
            model_name='building',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
        migrations.AlterField(
            model_name='building',
            name='osm_id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False, verbose_name='OSM ID'),
        ),
        migrations.AlterField(
            model_name='landuse',
            name='osm_id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False, verbose_name='OSM ID'),
        ),
        migrations.AlterField(
            model_name='natural',
            name='osm_id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False, verbose_name='OSM ID'),
        ),
        migrations.AlterField(
            model_name='naturala',
            name='osm_id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False, verbose_name='OSM ID'),
        ),
        migrations.AlterField(
            model_name='place',
            name='osm_id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False, verbose_name='OSM ID'),
        ),
        migrations.AlterField(
            model_name='placea',
            name='osm_id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False, verbose_name='OSM ID'),
        ),
        migrations.AlterField(
            model_name='pofw',
            name='osm_id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False, verbose_name='OSM ID'),
        ),
        migrations.AlterField(
            model_name='pofwa',
            name='osm_id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False, verbose_name='OSM ID'),
        ),
        migrations.AlterField(
            model_name='pois',
            name='osm_id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False, verbose_name='OSM ID'),
        ),
        migrations.AlterField(
            model_name='poisa',
            name='osm_id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False, verbose_name='OSM ID'),
        ),
        migrations.AlterField(
            model_name='railway',
            name='osm_id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False, verbose_name='OSM ID'),
        ),
        migrations.AlterField(
            model_name='road',
            name='osm_id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False, verbose_name='OSM ID'),
        ),
        migrations.AlterField(
            model_name='traffic',
            name='osm_id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False, verbose_name='OSM ID'),
        ),
        migrations.AlterField(
            model_name='traffica',
            name='osm_id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False, verbose_name='OSM ID'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='osm_id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False, verbose_name='OSM ID'),
        ),
        migrations.AlterField(
            model_name='transporta',
            name='osm_id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False, verbose_name='OSM ID'),
        ),
        migrations.AlterField(
            model_name='water',
            name='osm_id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False, verbose_name='OSM ID'),
        ),
        migrations.AlterField(
            model_name='waterway',
            name='osm_id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False, verbose_name='OSM ID'),
        ),
    ]
