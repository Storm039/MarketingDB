from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *


class CompanyApiInfo(generics.RetrieveUpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated,)


class ConfigDataApiInfo(generics.ListAPIView):
    serializer_class = ConfigDataSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        id_company = request.data.get("id_company", None)
        if not id_company:
            return Response({'error': "Method POST not allowed"})
        try:
            queryset = ConfigData.objects.filter(company=id_company)
        except:
            return Response({'error': "Object does not exists"})

        return Response({'result': ConfigDataSerializer(queryset, many=True).data})