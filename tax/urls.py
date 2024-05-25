from rest_framework.routers import DefaultRouter
from tax import views

router = DefaultRouter()
router.register(r'customers', views.CustomerViewSet) 
router.register(r'messages', views.MessageViewSet, basename='messages')
router.register(r'taxregions', views.TaxRegionViewSet)  

urlpatterns = router.urls