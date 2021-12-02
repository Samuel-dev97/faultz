from rest_framework.serializers import ModelSerializer
from .models import Fault


class FaultSerializer(ModelSerializer):
    class Meta:
        model = Fault
        fields = '__all__'