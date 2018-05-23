from django.contrib import admin

from .models import Project, HeroGeometry, BaseMap

admin.site.register(Project)
admin.site.register(HeroGeometry)
admin.site.register(BaseMap)