from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Message
from .serializers import MessageSerializer


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


@api_view()
def customer_detail(request, pk):
  return Response('OK')