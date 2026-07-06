from django.urls import path, include
from rest_framework.routers import DefaultRouter

from projects.views import ProjectViewSet, ProjectCategoryViewSet
from services.views import ServiceViewSet
from contact.views import ContactMessageViewSet
from core.views import CompanyProfileView

router = DefaultRouter()

# Projects
router.register(r"projects", ProjectViewSet, basename="projects")
router.register(r"categories", ProjectCategoryViewSet, basename="categories")

# Services
router.register(r"services", ServiceViewSet, basename="services")

# Contact
router.register(r"contact", ContactMessageViewSet, basename="contact")

urlpatterns = [
    path("", include(router.urls)),

    # single endpoint (not a viewset)
    path("company/", CompanyProfileView.as_view(), name="company"),
]