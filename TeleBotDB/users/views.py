from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *


class UsersApiList(APIView):
    serializer_class = UsersSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        self.permission_classes = (IsAdminUser,)
        queryset = Users.objects.all()
        return Response({'list_users': UsersSerializer(queryset, many=True).data})

    def post(self, request, *args, **kwargs):
        id_tbot = request.data.get("id_telegram", None)
        id_company = request.data.get("id_company", None)
        if not id_tbot or not id_company:
            return Response({'error': "Method POST not allowed"})
        try:
            queryset = Users.objects.filter(id_telegram=id_tbot,
                                            company=id_company)
        except:
            return Response({'error': "Object does not exists"})

        return Response({'result': UsersSerializer(queryset, many=True).data})


class ValidUsersApiList(APIView):
    serializer_class = UsersSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        id_company = request.data.get("id_company", None)
        if not id_company:
            return Response({'error': "Method POST not allowed"})
        try:
            queryset = Users.objects.filter(approval=True,
                                            create_1c=False,
                                            company=id_company)
        except:
            return Response({'error': "Object does not exists"})

        return Response({'result': UsersSerializer(queryset, many=True).data})


class UsersApiUpdate(generics.RetrieveUpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAuthenticated,)
    # включаем аутентификацию только по токену в данном методе (для JWT нужно отключить)
    # authentication_classes = (TokenAuthentication,)


class UsersApiDestroy(generics.RetrieveDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAdminUser,)


class UsersApiCreate(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAuthenticated,)
