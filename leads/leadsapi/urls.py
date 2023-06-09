from rest_framework import routers

from .api import LeadViewSet

# Create Here
router = routers.DefaultRouter()
router.register('leads', LeadViewSet, 'leads')

urlpatterns = router.urls