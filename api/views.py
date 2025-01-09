from pprint import pprint
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from website.models import Experience, Model, Deploiement
from .serializers import ExperienceSerializer, ModelSerializer, DeploiementSerializer
import joblib
import os
from django.conf import settings
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

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
    
class GetModelPredictionView(APIView):
    # permission_classes = [IsAuthenticated]
    
    def post(self, request, deploiement_id, *args, **kwargs):
       
        deploiement = Deploiement.objects.get(id=deploiement_id)
        pprint(deploiement.id)
        # dd(deploiement)
        if not Experience.DoesNotExist:
            return Response({'error': 'Experience ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            experience = Experience.objects.get(id=deploiement_id)
        except Experience.DoesNotExist:
            return Response({'error': 'Experience not found'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            deploiement = Deploiement.objects.get(experience=experience, state='PR', status='AC')
        except Deploiement.DoesNotExist:
            return Response({'error': 'No deployment found for this experience'}, status=status.HTTP_404_NOT_FOUND)
        
        model_path = os.path.join(settings.MEDIA_ROOT, str(deploiement.path))
        
        if not os.path.exists(model_path):
            return Response({'error': 'Model file not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Charger le modèle
        try:
            model = joblib.load(model_path)  # ou n'importe quel module pour charger votre modèle
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        # Effectuer des prédictions
        input_data = request.data.get('input_data')
        if not input_data:
            return Response({'error': 'Input data is required for prediction'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            predictions = model.predict(input_data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({'predictions': predictions}, status=status.HTTP_200_OK)