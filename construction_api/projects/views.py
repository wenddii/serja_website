from django.shortcuts import get_object_or_404, render

from core.context import site_context
from .models import Project


def projects_page(request):
    context = site_context()

    # Optional filtering by category via ?category=<name>
    category = request.GET.get('category')
    projects_qs = context['projects']
    if category:
        projects_qs = projects_qs.filter(category__name=category)

    context['projects'] = projects_qs
    context['project_count'] = projects_qs.count()
    return render(request, 'pages/projects.html', context)



def project_detail_page(request, slug):
    project = get_object_or_404(Project.objects.select_related('category'), slug=slug)
    context = site_context()
    context['project'] = project
    context['project_images'] = project.images.all()
    context['related_projects'] = Project.objects.exclude(pk=project.pk).select_related('category')[:3]
    return render(request, 'pages/project_detail.html', context)