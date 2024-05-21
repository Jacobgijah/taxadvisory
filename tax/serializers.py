from rest_framework import serializers
from tax.models import Customer


class CustomerSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  first_name = serializers.CharField(max_length=255)
  last_name = serializers.CharField(max_length=255)
  phone = serializers.CharField(max_length=13)


class MessageSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  message = serializers.CharField(max_length=255)
  message_alert = serializers.CharField(max_length=2)
  customer = serializers.HyperlinkedRelatedField(
    queryset=Customer.objects.all(),
    view_name='customer-detail'
  )