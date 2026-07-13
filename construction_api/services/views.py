from django.shortcuts import render

from core.context import site_context


def services_page(request):
    return render(request, 'pages/services.html', site_context())