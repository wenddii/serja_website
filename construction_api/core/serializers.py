from rest_framework import serializers
from .models import CompanyProfile


class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = [
            "id",
            "name",
            "description",
            "logo",
            "address",
            "phone",
            "email",
            "founded_year",
        ]