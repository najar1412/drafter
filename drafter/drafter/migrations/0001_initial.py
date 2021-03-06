# Generated by Django 2.0.5 on 2018-06-16 21:20

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('init_date', models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 6, 16, 21, 20, 35, 438402, tzinfo=utc))),
                ('image', models.CharField(default='default_basemap_image.jpg', max_length=200)),
                ('image_thumb', models.CharField(default='default_basemap_image_thumb.jpg', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.CharField(default='default_client_image.jpg', max_length=200)),
                ('image_thumb', models.CharField(default='default_client_image_thumb.jpg', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HeroGeometry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj_name', models.CharField(max_length=200)),
                ('init_date', models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 6, 16, 21, 20, 35, 439401, tzinfo=utc))),
                ('image', models.CharField(default='default_herogeometry_image.jpg', max_length=200)),
                ('image_thumb', models.CharField(default='default_herogeometry_image_thumb.jpg', max_length=200)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='drafter.Client')),
            ],
        ),
        migrations.CreateModel(
            name='InstanceMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.CharField(default='default_instancemap_image.jpg', max_length=200)),
                ('image_thumb', models.CharField(default='default_instancemap_image_thumb.jpg', max_length=200)),
                ('init_date', models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 6, 16, 21, 20, 35, 438402, tzinfo=utc))),
                ('basemap', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='drafter.BaseMap')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('init_date', models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 6, 16, 21, 20, 35, 437402, tzinfo=utc))),
                ('image', models.CharField(default='default_project_image.jpg', max_length=200)),
                ('image_thumb', models.CharField(default='default_project_image_thumb.jpg', max_length=200)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drafter.Client')),
            ],
        ),
        migrations.AddField(
            model_name='instancemap',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drafter.Project'),
        ),
        migrations.AddField(
            model_name='herogeometry',
            name='instancemaps',
            field=models.ManyToManyField(to='drafter.InstanceMap'),
        ),
    ]
