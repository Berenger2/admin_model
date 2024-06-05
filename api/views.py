from django.shortcuts import render
from rest_framework import viewsets
from website.models import Experience, Model, Deploiement
from .serializers import ExperienceSerializer, ModelSerializer, DeploiementSerializer

class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class DeploiementViewSet(viewsets.ModelViewSet):
    queryset = Deploiement.objects.all()
    serializer_class = DeploiementSerializer


