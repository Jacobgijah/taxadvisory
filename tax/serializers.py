from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  message = serializers.CharField(max_length=255)
  message_alert = serializers.CharField(max_length=2)