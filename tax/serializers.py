from rest_framework import serializers
from tax.models import Message, Customer, TaxRegion


class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields = ['id', 'first_name', 'last_name', 'phone', 'email',
               'organization_type', 'organization_name', 'messages_count']

  messages_count = serializers.IntegerField(read_only=True)


class MessageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Message
    fields = ['id', 'message', 'message_alert', 'customer']

  # customer = serializers.HyperlinkedRelatedField(
  #   queryset=Customer.objects.all(),
  #   view_name='customer-detail'
  # )


class TaxRegionSerializer(serializers.ModelSerializer):
  class Meta:
    model = TaxRegion
    fields = ['customer', 'region', 'district']