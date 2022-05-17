from datetime import datetime
from django.db.models import Q
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import *
from .serializer import *


class PromotionsApiList(APIView):
    serializer_class = PromotionsSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        company = request.data.get("id_company", None)
        if not company:
            return Response({'error': "Method POST not allowed"})
        try:
            queryset = Promotions.objects.filter(
                Q(activity=True) & Q(company=company) &
                (Q(date_start__lte=datetime.now()) | Q(date_end__gte=datetime.now()))
            )
        except:
            return Response({'error': "Object does not exists"})

        return Response({'result': PromotionsSerializer(queryset, many=True).data})


class PromotionsApiCreate(generics.CreateAPIView):
    serializer_class = PromotionsSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Promotions.objects.all()


class BonusesApiUpdate(APIView):
    serializer_class = BonusesSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        id_user = request.data.get("user", None)
        if not id_user:
            return Response({'error': "Method POST not allowed"})

        try:
            user_obj = Users.objects.get(pk=id_user)
        except Users.DoesNotExist:
            return Response(f"The user with the specified pk does not exist")

        try:
            obj = Bonuses.objects.get(user=id_user)
            for key, value in request.data.items():
                if key == "user":
                    value = user_obj
                setattr(obj, key, value)
            obj.save()
        except Bonuses.DoesNotExist:
            new_values = {'user': user_obj, 'quantity': request.data.get("quantity")}
            obj = Bonuses(**new_values)
            obj.save()
        return Response(f"Process complete")


class BonusesApiInfo(APIView):
    serializer_class = BonusesSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.data.get("id_user", None)
        if not user:
            return Response({'error': "Method POST not allowed"})
        try:
            queryset = Bonuses.objects.filter(user=user)
        except:
            return Response({'error': "Object does not exists"})

        return Response({'result': BonusesSerializer(queryset, many=True).data})
