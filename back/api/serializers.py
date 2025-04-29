from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class SensoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensores
        many = True
        fields = '__all__'

class AmbientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambientes
        many = True
        fields = '__all__'   

class HistoricosSerializer(serializers.ModelSerializer):
    sensor = SensoresSerializer(read_only=True)
    sensor_id = serializers.PrimaryKeyRelatedField(
        queryset = Sensores.objects.all(), source='sensor', write_only=True
    )
    
    ambiente = AmbientesSerializer(read_only=True)
    ambiente_id = serializers.PrimaryKeyRelatedField(
        queryset = Ambientes.objects.all(), source='ambientes', write_only=True
    )

    class Meta:
        model = Historicos
        fields = ['id', 'sensor', 'ambiente', 'observacoes']