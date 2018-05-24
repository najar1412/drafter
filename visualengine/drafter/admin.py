from django.contrib import admin

from .models import Project, HeroGeometry, BaseMap, Client ,InstanceMap

admin.site.register(Project)
admin.site.register(HeroGeometry)
admin.site.register(BaseMap)
admin.site.register(Client)
admin.site.register(InstanceMap)