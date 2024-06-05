from rest_framework import routers

from .views import ModelViewSet, ExperienceViewSet, DeploiementViewSet

router = routers.DefaultRouter()
router.register('model', ModelViewSet)
router.register('experience', ExperienceViewSet)
router.register('deploiement', DeploiementViewSet)
