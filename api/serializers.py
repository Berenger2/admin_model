from rest_framework import serializers
from website.models import Experience, Model, Deploiement

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'
class DeploiementSerializer(serializers.ModelSerializer):
    model = ModelSerializer()
    experience = ExperienceSerializer()

    class Meta:
        model = Deploiement
        fields = '__all__'