from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Project, Client, InstanceMap, HeroGeometry
from .helpers import to_dict


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
        'client': to_dict(Client.objects.get(pk=client_id)),
        'project': [to_dict(x) for x in Project.objects.all()]
        }

    return render(request, 'client.html', context)


def project_map(request, client_id, project_id, instancemap_id):
    context = {
        'map': to_dict(InstanceMap.objects.get(pk=project_id)),
        'project': to_dict(Project.objects.get(pk=instancemap_id))
    }

    return render(request, 'instancemap.html', context)


def project_geometries(request, client_id, project_id):
    return render(request, 'geometries.html')


def project_geometry(request, client_id, project_id, geometry_id):
    # TODO: broken. fix.
    context = {
        'geometry': HeroGeometry.objects.get(pk=geometry_id)
    }

    return render(request, 'geometry.html', context)


def projects(request, client_id):
    latest_projects = Project.objects.order_by('-init_date')[:5].values()
    context = {'latest_projects': latest_projects}

    return render(request, 'projects.html', context)


def project(request, client_id, project_id):
    context = {
        'project': to_dict(get_object_or_404(Project, pk=project_id)),
        'maps': [to_dict(x) for x in InstanceMap.objects.all()],
        'geometry': [x for x in HeroGeometry.objects.all()]
    }

    return render(request, 'project.html', context)


def project_maps(request, client_id, project_id):
    return HttpResponse("project maps")


