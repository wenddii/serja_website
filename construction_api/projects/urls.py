from django.urls import path

from .views import project_detail_page, projects_page

urlpatterns = [
    path('', projects_page, name='projects'),
    path('<slug:slug>/', project_detail_page, name='project_detail'),
]