from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import Message, Customer, TaxRegion
from .serializers import MessageSerializer, CustomerSerializer, TaxRegionSerializer


class MessageViewSet(ModelViewSet):
  queryset = Message.objects.select_related('customer').all()
  serializer_class = MessageSerializer

  def get_serializer_context(self):
     return {'request': self.request}

  def delete(self, request, pk):
    message = get_object_or_404(Message, pk=pk)
    message.delete()
    return Response({'success': 'Message deleted'}, status=status.HTTP_204_NO_CONTENT)


class CustomerViewSet(ModelViewSet):
  queryset = Customer.objects.annotate(messages_count=Count('messages')).all()
  serializer_class = CustomerSerializer

  def delete(self, request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return Response({'success': 'Customer deleted'}, status=status.HTTP_204_NO_CONTENT)


class TaxRegionViewSet(ModelViewSet):
  queryset = TaxRegion.objects.all()
  serializer_class = TaxRegionSerializer