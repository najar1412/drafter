from django.urls import path

from . import views


app_name = 'drafter'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),

    path('<int:client_id>/', views.client, name='client'),
    
    path('<int:client_id>/projects/', views.projects, name='projects'),
    path('<int:client_id>/<int:project_id>/', views.project, name='project'),

    path('<int:client_id>/<int:project_id>/maps/', views.project_maps, name='project_maps'),
    path('<int:client_id>/<int:project_id>/map/<int:instancemap_id>/', views.project_map, name='project_map'),

    path('<int:client_id>/<int:project_id>/geometries/', views.project_geometries, name='project_geometries'),
    path('<int:client_id>/<int:project_id>/geometry/<int:geometry_id>/', views.project_geometry, name='project_geometry'),
]

