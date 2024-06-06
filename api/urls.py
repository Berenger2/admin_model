from rest_framework import routers
from django.urls import path, include

from .views import ModelViewSet, ExperienceViewSet, DeploiementViewSet,ExperienceFilteredListView, DeploiementFilteredListView, DeploiementProdListView

router = routers.DefaultRouter()
router.register(r'model', ModelViewSet)
router.register(r'experience', ExperienceViewSet)
router.register(r'deploiement', DeploiementViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('experiences/prod/', ExperienceFilteredListView.as_view(), name='experience-filtered-list'),
    path('deploiements/pr/', DeploiementProdListView.as_view(), name='deploiement-filtered-list'),
]