from rest_framework import serializers
from .models import *


class PromotionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotions
        fields = "__all__"


class BonusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonuses
        fields = "__all__"
