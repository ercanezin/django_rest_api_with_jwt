from rest_framework import serializers
from .models import Logs


class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = ('id', 'user', 'user_name', 'user_ip', 'user_agent_info', 'login_status', 'attempted_at')
