from django.urls import path

from . import views


app_name = 'drafter'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:client_id>/projects/', views.projects, name='projects'),
    path('<int:client_id>/<int:project_id>/', views.project, name='project'),
    path('<int:client_id>/<int:project_id>/maps/', views.project_maps, name='project_maps'),
    path('<int:client_id>/<int:project_id>/geometry/', views.project_geometry, name='project_geometry'),
]

