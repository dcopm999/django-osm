# Generated by Django 3.1.5 on 2021-05-10 13:32

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('osm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShapeFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='URL')),
                ('filename', models.FileField(upload_to='gdal', verbose_name='File name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Shape file',
                'verbose_name_plural': 'Shape files',
            },
        ),
        migrations.AlterModelOptions(
            name='building',
            options={'ordering': ['-id'], 'verbose_name': 'Building', 'verbose_name_plural': 'Buildings'},
        ),
        migrations.AlterModelOptions(
            name='landuse',
            options={'ordering': ['-id'], 'verbose_name': 'Landuse', 'verbose_name_plural': 'Landuses'},
        ),
        migrations.AlterModelOptions(
            name='natural',
            options={'ordering': ['-id'], 'verbose_name': 'Natural', 'verbose_name_plural': 'Naturals'},
        ),
        migrations.AlterModelOptions(
            name='naturala',
            options={'ordering': ['-id'], 'verbose_name': 'Natural A', 'verbose_name_plural': 'Naturals A'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['-id'], 'verbose_name': 'Place', 'verbose_name_plural': 'Places'},
        ),
        migrations.AlterModelOptions(
            name='placea',
            options={'ordering': ['-id'], 'verbose_name': 'Place A', 'verbose_name_plural': 'Places A'},
        ),
        migrations.AlterModelOptions(
            name='pofw',
            options={'ordering': ['-id'], 'verbose_name': 'Pofw', 'verbose_name_plural': 'Pofws'},
        ),
        migrations.AlterModelOptions(
            name='pofwa',
            options={'ordering': ['-id'], 'verbose_name': 'Pofw A', 'verbose_name_plural': 'Pofws A'},
        ),
        migrations.AlterModelOptions(
            name='pois',
            options={'ordering': ['-id'], 'verbose_name': 'Pois', 'verbose_name_plural': 'Poises'},
        ),
        migrations.AlterModelOptions(
            name='poisa',
            options={'ordering': ['-id'], 'verbose_name': 'Pois A', 'verbose_name_plural': 'Poises A'},
        ),
        migrations.AlterModelOptions(
            name='railway',
            options={'ordering': ['-id'], 'verbose_name': 'RailWay', 'verbose_name_plural': 'RailWays'},
        ),
        migrations.AlterModelOptions(
            name='road',
            options={'ordering': ['-id'], 'verbose_name': 'Road', 'verbose_name_plural': 'Roads'},
        ),
        migrations.AlterModelOptions(
            name='traffic',
            options={'ordering': ['-id'], 'verbose_name': 'Traffic', 'verbose_name_plural': 'Traffics'},
        ),
        migrations.AlterModelOptions(
            name='traffica',
            options={'ordering': ['-id'], 'verbose_name': 'Traffic A', 'verbose_name_plural': 'Traffics A'},
        ),
        migrations.AlterModelOptions(
            name='transport',
            options={'ordering': ['-id'], 'verbose_name': 'Transport', 'verbose_name_plural': 'Transports'},
        ),
        migrations.AlterModelOptions(
            name='transporta',
            options={'ordering': ['-id'], 'verbose_name': 'Transport A', 'verbose_name_plural': 'Transports A'},
        ),
        migrations.AlterModelOptions(
            name='water',
            options={'ordering': ['-id'], 'verbose_name': 'Water', 'verbose_name_plural': 'Waters'},
        ),
        migrations.AlterModelOptions(
            name='waterway',
            options={'ordering': ['-id'], 'verbose_name': 'Water Way', 'verbose_name_plural': 'WaterWays'},
        ),
        migrations.AddField(
            model_name='building',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='building',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted'),
        ),
        migrations.AddField(
            model_name='building',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='landuse',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landuse',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted'),
        ),
        migrations.AddField(
            model_name='landuse',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='natural',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='natural',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted'),
        ),
        migrations.AddField(
            model_name='natural',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='naturala',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='naturala',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted'),
        ),
        migrations.AddField(
            model_name='naturala',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='place',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted'),
        ),
        migrations.AddField(
            model_name='place',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='placea',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='placea',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted'),
        ),
        migrations.AddField(
            model_name='placea',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='pofw',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pofw',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted'),
        ),
        migrations.AddField(
            model_name='pofw',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='pofwa',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pofwa',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted'),
        ),
        migrations.AddField(
            model_name='pofwa',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='pois',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pois',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted'),
        ),
        migrations.AddField(
            model_name='pois',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='poisa',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poisa',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted'),
        ),
        migrations.AddField(
            model_name='poisa',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='railway',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='railway',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted'),
        ),
        migrations.AddField(
            model_name='railway',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='road',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='road',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted'),
        ),
        migrations.AddField(
            model_name='road',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='traffic',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traffic',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted'),
        ),
        migrations.AddField(
            model_name='traffic',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='traffica',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traffica',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted'),
        ),
        migrations.AddField(
            model_name='traffica',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='transport',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transport',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted'),
        ),
        migrations.AddField(
            model_name='transport',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='transporta',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transporta',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted'),
        ),
        migrations.AddField(
            model_name='transporta',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='water',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='water',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted'),
        ),
        migrations.AddField(
            model_name='water',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='waterway',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='waterway',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted'),
        ),
        migrations.AddField(
            model_name='waterway',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='world',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='world',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted'),
        ),
        migrations.AddField(
            model_name='world',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='building',
            name='geom',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326),
        ),
        migrations.AlterField(
            model_name='natural',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
    ]
