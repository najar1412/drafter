import datetime

from django.db import models
from django.utils import timezone


class Client(models.Model):
    """drafter client"""
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200, default='default_client_image.jpg')
    image_thumb = models.CharField(max_length=200, default='default_client_image_thumb.jpg')

    def __str__(self):
        return f'{self.name}'


class Project(models.Model):
    """darfter project"""
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    init_date = models.DateTimeField(timezone.now(), null=True)
    image = models.CharField(max_length=200, default='default_project_image.jpg')
    image_thumb = models.CharField(max_length=200, default='default_project_image_thumb.jpg')

    def __str__(self):
        return f'{self.name}'


class BaseMap(models.Model):
    """premade maps"""
    name = models.CharField(max_length=200)
    init_date = models.DateTimeField(timezone.now(), null=True)
    image = models.CharField(max_length=200, default='default_basemap_image.jpg')
    image_thumb = models.CharField(max_length=200, default='default_basemap_image_thumb.jpg')

    def __str__(self):
        return f'{self.name}'


class InstanceMap(models.Model):
    """client map, after customisation of a basemap"""
    name = models.CharField(max_length=200)
    basemap = models.ForeignKey(BaseMap, null=True, on_delete=models.SET_NULL)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.CharField(max_length=200, default='default_instancemap_image.jpg')
    image_thumb = models.CharField(max_length=200, default='default_instancemap_image_thumb.jpg')
    init_date = models.DateTimeField(timezone.now(), null=True)


    def __str__(self):
        return f'{self.name}'


class HeroGeometry(models.Model):
    """clients low poly schemes"""
    obj_name = models.CharField(max_length=200)
    init_date = models.DateTimeField(timezone.now(), null=True)
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    instancemaps = models.ManyToManyField(InstanceMap)
    image = models.CharField(max_length=200, default='default_herogeometry_image.jpg')
    image_thumb = models.CharField(max_length=200, default='default_herogeometry_image_thumb.jpg')

    def __str__(self):
        return f'{self.obj_name}'