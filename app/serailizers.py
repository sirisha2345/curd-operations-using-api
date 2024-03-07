from rest_framework import serializers
from app.models import *
class empModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=emp
        fields='__all__'