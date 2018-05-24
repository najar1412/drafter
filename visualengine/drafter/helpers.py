"""
Contains database related source code
"""

from django.db.models.fields.related import ManyToManyField
from django.shortcuts import get_object_or_404

from .models import Client, Project, InstanceMap, HeroGeometry, BaseMap


def to_dict(instance):
    """doenst not work on querySets"""
    opts = instance._meta
    data = {}
    for f in opts.concrete_fields + opts.many_to_many:
        if isinstance(f, ManyToManyField):
            if instance.pk is None:
                data[f.name] = []
            else:
                data[f.name] = list(f.value_from_object(instance).values_list('pk', flat=True))
        else:
            data[f.name] = f.value_from_object(instance)
    return data


class ClientHandler():
    """Client interaction"""
    _MODEL = {
        'id': None,
        'name': None,
        'image': None
    }

    def _to_dict(self, obj):
        result = self._MODEL
        result['id'] = obj.pk
        result['name'] = obj.name
        result['image'] = obj.image

        return result


    def __init__(self):
        pass


    def get(self, pk):
        return self._to_dict(Client.objects.get(pk=pk))


    def all(self):
        result = []
        clients = Client.objects.all()
        for client in clients:
            result.append(self._to_dict(client))

        return result


    def __repr__(self):
        return '<Client>'


class ProjectHandler():
    """Project interaction"""
    _MODEL = {
        'id': None,
        'client': None,
        'name': None,
        'init_date': None,
        'image': None
    }

    def __init__(self):
        pass

    def _to_dict(self, obj):
        result = self._MODEL
        result['id'] = obj.id
        result['client'] = obj.client
        result['name'] = obj.name
        result['init_date'] = obj.init_date
        result['image'] = obj.image

        return result


    def get(self, pk):
        return self._to_dict(Project.objects.get(pk=pk))


    def all(self, orderby=None, quantity=None):
        result = []

        if not orderby and not quantity:
            projects = Project.objects.all()
            for project in projects:
                result.append(self._to_dict(project).copy())

            return result


        elif not orderby and quantity:
            projects = Project.objects.all()[:quantity]
            for project in projects:
                result.append(project.copy())

            return result


        elif orderby and orderby in self._MODEL:
            projects = Project.objects.order_by(f'-{orderby}')
            if quantity:
                return projects[:quantity].values()



    def __repr__(self):
        return '<Project>'


class InstanceMapHandler():
    """Project interaction"""
    _MODEL = {
        'name': None,
        'basemap': None,
        'project': None,
        'image': None
    }

    def __init__(self):
        pass

    def _to_dict(self, obj):
        result = self._MODEL
        result['id'] = obj.pk
        result['name'] = obj.name
        result['basemap'] = obj.basemap
        result['project'] = obj.project
        result['image'] = obj.image

        self._MODEL = self._MODEL

        return result


    def get(self, pk):
        return self._to_dict(InstanceMap.objects.get(pk=pk))


    def all(self):
        # maps = InstanceMap.objects.all()
        results = []
        for ma in InstanceMap.objects.all():
            results.append(self._to_dict(ma).copy())

        return results


    def __repr__(self):
        return '<InstanceMap>'


class HeroGeometryHandler():
    _MODEL = {
        'obj_name': None,
        'init_date': None,
        'client': None,
        'instancemaps': None,
        'image': None
    }


    def __init__(self):
        pass


    def _to_dict(self, obj):
        result = self._MODEL
        result['obj_name'] = obj.obj_name
        result['init_date'] = obj.init_date
        result['client'] = obj.client
        result['instancemaps'] = obj.instancemaps
        result['image'] = obj.image

        return result


    def get(self, pk):
        return self._to_dict(HeroGeometry.objects.get(pk=pk))


    def all(self):
        return HeroGeometry.objects.all()


    def __repr__(self):
        return '<HeroGeometry>'