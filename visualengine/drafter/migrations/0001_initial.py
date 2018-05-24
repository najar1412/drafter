# Generated by Django 2.0.5 on 2018-05-23 18:34

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
                ('init_date', models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 5, 23, 18, 34, 46, 207925, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HeroGeometry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj_name', models.CharField(max_length=200)),
                ('init_date', models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 5, 23, 18, 34, 46, 207925, tzinfo=utc))),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='drafter.Client')),
            ],
        ),
        migrations.CreateModel(
            name='InstanceMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('basemap', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='drafter.BaseMap')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('init_date', models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 5, 23, 18, 34, 46, 206926, tzinfo=utc))),
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
