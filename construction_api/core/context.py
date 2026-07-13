from projects.models import Project
from services.models import Service
from machinery.models import Machinery

from .models import CompanyProfile, Testimonial


def site_context():
    company = CompanyProfile.objects.first()
    return {
        'company': company,
        'services': Service.objects.all().order_by('title'),
        'projects': Project.objects.select_related('category').order_by('-created_at'),
        'project_categories': Project.objects.select_related('category').values_list('category__name', flat=True).distinct(),
        "machineries": Machinery.objects.all().order_by("name"),
        "testimonials": Testimonial.objects.filter(is_active=True).order_by("-id"),
    }

