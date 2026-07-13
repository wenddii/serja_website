from django.contrib import admin
from .models import Project, ProjectCategory, ProjectImage


admin.site.register(Project)
admin.site.register(ProjectCategory)
admin.site.register(ProjectImage)