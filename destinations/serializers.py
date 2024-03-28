from rest_framework import serializers
from .models import Destination
class Desination_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields ='__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']