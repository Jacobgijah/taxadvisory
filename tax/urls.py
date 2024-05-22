from django.urls import path, include
from rest_framework import routers
from tax import views

router = routers.DefaultRouter()
router.register('messages', views.MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('messages/', views.MessageList.as_view()),
    # path('messages/<int:pk>/', views.MessageDetail.as_view()),
    path('customers/', views.CustomerList.as_view()),
    path('customers/<int:pk>/', views.CustomerDetail.as_view(), name='customer-detail'),
]