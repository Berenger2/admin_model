from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
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

"""Filtering the experiences by status and state"""
class ExperienceFilteredListView(generics.ListAPIView):
    serializer_class = ExperienceSerializer

    def get_queryset(self):
        return Experience.objects.filter(status="AC", state="PR")
    
"""Filtering the deploiement by status and state"""
class DeploiementFilteredListView(generics.ListAPIView):
    serializer_class = DeploiementSerializer

    def get_queryset(self):
        return Deploiement.objects.filter(status="AC", state="PR")
    
    
class DeploiementProdListView(APIView):
    def get(self, request):
        deploiements = Deploiement.objects.filter(state='PR', status='AC')
        serializer = DeploiementSerializer(deploiements, many=True)
        return Response(serializer.data)