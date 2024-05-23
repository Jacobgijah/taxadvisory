from rest_framework.routers import DefaultRouter
from tax import views

router = DefaultRouter()
router.register(r'messages', views.MessageViewSet)
router.register(r'customers', views.CustomerViewSet) 
router.register(r'taxregions', views.TaxRegionViewSet) 

urlpatterns = router.urls