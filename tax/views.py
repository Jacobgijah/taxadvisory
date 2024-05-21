from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
    return Response('OK')

@api_view()
def message_detail(request, id):
  message = get_object_or_404(Message, pk=id)
  serializer = MessageSerializer(message, context={'request': request}) # dictionary of message
  return Response(serializer.data)

@api_view()
def customer_detail(request, pk):
  return Response('OK')