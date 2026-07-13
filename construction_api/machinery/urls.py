from django.urls import path
from . import views

app_name = "machinery"

urlpatterns = [
    path("", views.machinery_list, name="list"),
    path("<int:pk>/", views.machinery_detail, name="detail"),
]