from django.urls import path

from . import views


app_name = 'drafter'
urlpatterns = [
    path('', views.login, name='login'),

    path('<int:client_id>/', views.client, name='client'),
    path('<int:client_id>/<int:project_id>/', views.project, name='project'),
    path('<int:client_id>/<int:project_id>/map/<int:instancemap_id>/', views.project_map, name='project_map'),
    path('<int:client_id>/<int:project_id>/geometry/<int:geometry_id>/', views.project_geometry, name='project_geometry'),
]

