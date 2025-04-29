from django.shortcuts import render

from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User


class SignUpView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SensoresView(ListCreateAPIView):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer
    permission_classes = [IsAuthenticated]

class SensoresAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer
    permission_classes = [IsAuthenticated]

class AmbientesView(ListCreateAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializer
    permission_classes = [IsAuthenticated]

class AmbientesAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializer
    permission_classes = [IsAuthenticated]

class HistoricosView(ListCreateAPIView):
    queryset = Historicos.objects.all()
    serializer_class = HistoricosSerializer
    permission_classes = [IsAuthenticated]

class HistoricosAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Historicos.objects.all()
    serializer_class = HistoricosSerializer
    permission_classes = [IsAuthenticated]