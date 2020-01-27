from rest_framework import serializers
from .models import notification
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = notification
        fields = ('name','title','date_added','status')