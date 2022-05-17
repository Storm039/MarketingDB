from rest_framework import serializers
from .models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class ConfigDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigData
        fields = "__all__"


