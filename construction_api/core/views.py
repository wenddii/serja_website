from .context import site_context
from django.shortcuts import render


def home_page(request):
    context = site_context()
    context['featured_projects'] = context['projects'][:3]
    context['featured_services'] = context['services'][:3]
    context["featured_testimonials"] = context["testimonials"][:3]
    context["featured_machineries"] = context["machineries"][:6]
    return render(request, 'pages/home.html', context)


def about_page(request):
    return render(request, 'pages/about.html', site_context())


