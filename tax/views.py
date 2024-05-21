from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def message_list(request):
  return Response('ok')


@api_view()
def message_detail(request, id):
  return Response(id)