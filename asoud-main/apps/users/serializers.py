from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = User
        fields = [
            'id', 
            'mobile_number'
        ]