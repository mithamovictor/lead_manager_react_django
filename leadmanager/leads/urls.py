from rest_framework import routers
from .api import LeadViewset

router = routers.DefaultRouter()
router.register( 'api/leads', LeadViewset, 'leads' )

# Get registered urls for 'api/leads' endpoint
urlpatterns = router.urls
