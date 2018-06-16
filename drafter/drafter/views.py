import json

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.urls import reverse

from .helpers import ClientHandler, ProjectHandler, InstanceMapHandler, HeroGeometryHandler
from .modules import SceneData

def login(request):
    return render(request, 'login.html')


def dev_engine(request):
    return render(request, 'dev_engine.html')


def client(request, client_id):
    context = {
        'client': ClientHandler().get(client_id),
        'project': ProjectHandler().all()
        }

    return render(request, 'client.html', context)


def project_map(request, client_id, project_id, instancemap_id):
    # TODO: flesh out json object that has all scene data per map.
    # TODO: seems i cant send one object from django and convert to 
    # both an object (for templating) and object for javascript on the client side?
    scene_cameras = SceneData().encode_cameras(encode=False)

    context = {
        'map': InstanceMapHandler().get(instancemap_id),
        'project': ProjectHandler().get(project_id),
        'client': ClientHandler().get(client_id),
        'scene_cameras': scene_cameras
    }

    return render(request, 'components/map.html', context)


def project_geometries(request, client_id, project_id):
    return render(request, 'geometries.html')


def project_geometry(request, client_id, project_id, geometry_id):
    # TODO: broken. fix.
    context = {
        'geometry': HeroGeometryHandler().get(geometry_id),
        'project': ProjectHandler().get(project_id),
        'client': ClientHandler().get(client_id)
    }

    return render(request, 'geometry.html', context)



def project(request, client_id, project_id):
    context = {
        'client': ClientHandler().get(pk=client_id),
        'project': ProjectHandler().get(project_id),
        'maps': InstanceMapHandler().all(),
        'geometry': HeroGeometryHandler().all()
    }

    return render(request, 'project.html', context)

