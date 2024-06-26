from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .filters import MessageFilter
from .models import Message, Customer, TaxRegion
from .serializers import MessageSerializer, CustomerSerializer, TaxRegionSerializer


class MessageViewSet(ModelViewSet):
  queryset = Message.objects.all()
  serializer_class = MessageSerializer
  filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
  filterset_class = MessageFilter
  search_fields = ['message_alert']
  ordering_fields = ['created_at']

  def get_serializer_context(self):
     return {'request': self.request}
  
  def destroy(self, request, *args, **kwargs):
    return super().destroy(request, *args, **kwargs)



class CustomerViewSet(ModelViewSet):
  queryset = Customer.objects.annotate(messages_count=Count('messages')).all()
  serializer_class = CustomerSerializer

  def destroy(self, request, *args, **kwargs):
    return super().destroy(request, *args, **kwargs)

class TaxRegionViewSet(ModelViewSet):
  queryset = TaxRegion.objects.all()
  serializer_class = TaxRegionSerializer

