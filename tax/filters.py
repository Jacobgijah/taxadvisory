from django_filters.rest_framework import FilterSet
from .models import Message

class MessageFilter(FilterSet):
  class Meta:
    model = Message
    fields = {
      'customer_id': ['exact'],
    }