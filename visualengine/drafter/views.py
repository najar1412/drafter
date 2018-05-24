from django.shortcuts import render
from django.urls import reverse

from .helpers import ClientHandler, ProjectHandler, InstanceMapHandler, HeroGeometryHandler


def index(request):
    return render(request, 'index.html')


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
    context = {
        'map': InstanceMapHandler().get(instancemap_id),
        'project': ProjectHandler().get(project_id)
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

