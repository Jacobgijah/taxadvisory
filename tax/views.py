from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer


@api_view()
def message_list(request):
  queryset = Message.objects.all()
  serializer = MessageSerializer(queryset, many=True)
  return Response(serializer.data)


@api_view()
def message_detail(request, id):
  message = get_object_or_404(Message, pk=id)
  serializer = MessageSerializer(message) # dictionary of message
  return Response(serializer.data)