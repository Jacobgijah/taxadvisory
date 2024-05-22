from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Message, Customer
from .serializers import MessageSerializer, CustomerSerializer


@api_view(['GET', 'POST'])
def message_list(request):
  if request.method == 'GET':
    queryset = Message.objects.select_related('customer').all()
    serializer = MessageSerializer(queryset, many=True, context={'request': request})
    return Response(serializer.data)
  
  elif request.method == 'POST':
    serializer = MessageSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  

@api_view(['GET', 'PUT', 'DELETE'])
def message_detail(request, id):
  message = get_object_or_404(Message, pk=id)
  if request.method == 'GET':
    serializer = MessageSerializer(message, context={'request': request}) # dictionary of message
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = MessageSerializer(message, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  
  elif request.method == 'DELETE':
    message.delete()
    return Response({'success': 'Message deleted'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def customer_list(request):
  if request.method == 'GET':
    queryset = Customer.objects.annotate(messages_count=Count('messages')).all()
    serializer = CustomerSerializer(queryset, many=True)
    return Response(serializer.data)
  
  elif request.method == 'POST':
    serializer = CustomerSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request, pk):
  customer = get_object_or_404(
    Customer.objects.annotate(messages_count=Count('messages'), pk=pk)
  )

  if request.method == 'GET':
    serializer = CustomerSerializer(Customer)
    return Response(serializer.data)
  
  elif request.method == 'PUT':
    serializer = CustomerSerializer(Customer, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  
  elif request.method == 'DELETE':
    customer.delete()
    return Response({'success': 'Customer deleted'}, status=status.HTTP_204_NO_CONTENT)
  