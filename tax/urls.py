from django.urls import path
from tax import views

urlpatterns = [
    path('', views.index, name='index'),
]