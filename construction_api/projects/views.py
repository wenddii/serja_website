from rest_framework import viewsets
from .models import ProjectCategory, Project
from .serializers import ProjectCategorySerializer, ProjectSerializer


class ProjectCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.select_related("category").prefetch_related("images")
    serializer_class = ProjectSerializer
    lookup_field = "slug"