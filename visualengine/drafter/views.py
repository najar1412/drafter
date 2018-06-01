import json

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.urls import reverse

from .helpers import ClientHandler, ProjectHandler, InstanceMapHandler, HeroGeometryHandler


def index(request):
    return render(request, 'index.html')


def dev_engine(request):
    return render(request, 'dev_engine.html')


def upload(request):
    if 'POST' in request:
        # this is not how to look for a post request. fix.
        upload_type = request.POST['choice']

        return render(request, 'uploadsuccess.html', {'upload_type': upload_type})


    else:
        context = {
            'upload_type': ['project', 'map', 'geometry', 'client']
        }

        return render(request, 'upload.html', context)


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
    params = {
        'cameras': 
            {
                'default': {
                    'fov': 40,
                    'pos': [650, 250, -900],
                    'rot': [0, -180, 0]
                },
                'cam01': {},
                'cam02': {}
            },
        
    }

    params_json = json.dumps(dict(params), cls=DjangoJSONEncoder)

    context = {
        'map': InstanceMapHandler().get(instancemap_id),
        'project': ProjectHandler().get(project_id),
        'client': ClientHandler().get(client_id),
        'params': params_json
    }

    return render(request, 'instancemap.html', context)


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


def projects(request, client_id):
    context = {
        'projects': ProjectHandler().all(orderby='init_date', quantity=5),
        'client': ClientHandler().get(pk=client_id)
        }

    return render(request, 'projects.html', context)


def project(request, client_id, project_id):
    context = {
        'client': ClientHandler().get(pk=client_id),
        'project': ProjectHandler().get(project_id),
        'maps': InstanceMapHandler().all(),
        'geometry': HeroGeometryHandler().all()
    }

    return render(request, 'project.html', context)

