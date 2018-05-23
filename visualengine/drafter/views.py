from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Project


# Create your views here.
def index(request):
    return render(request, 'drafter/index.html')


def projects(request, client_id):
    latest_projects = Project.objects.order_by('-init_date')[:5]
    context = {'latest_projects': latest_projects}

    return render(request, 'drafter/projects.html', context)


def project(request, client_id, project_id):
    project = get_object_or_404(Project, pk=project_id)

    return render(request, 'drafter/project', {'project': project})




def project_maps(request, client_id, project_id):
    return HttpResponse("maps for project {self.project_id}, client {self.client_id}")


def project_geometry(request, client_id, project_id):
    return HttpResponse("hero geometry page for project {self.project_id}")
