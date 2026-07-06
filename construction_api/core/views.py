from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CompanyProfile
from .serializers import CompanyProfileSerializer


class CompanyProfileView(APIView):
    def get(self, request):
        company = CompanyProfile.objects.first()
        serializer = CompanyProfileSerializer(company)
        return Response(serializer.data)