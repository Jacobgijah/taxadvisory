from django.urls import path
from tax import views

urlpatterns = [
    path('messages/', views.message_list),
    path('messages/<int:id>/', views.message_detail),
]