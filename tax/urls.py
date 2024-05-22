from django.urls import path
from tax import views

urlpatterns = [
    path('messages/', views.message_list),
    path('messages/<int:id>/', views.message_detail),
    path('customers/', views.customer_list),
    path('customers/<int:pk>/', views.customer_detail, name='customer-detail'),
]