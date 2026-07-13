from django.shortcuts import get_object_or_404, render

from core.context import site_context
from .models import Machinery


def machinery_list(request):
    context = site_context()
    context["machineries"] = Machinery.objects.all().order_by("name")
    return render(request, "pages/machinery.html", context)


def machinery_detail(request, pk):
    context = site_context()
    context["machinery"] = get_object_or_404(Machinery, pk=pk)
    context["machineries"] = Machinery.objects.all().order_by("name")
    return render(request, "pages/machinery_detail.html", context)
