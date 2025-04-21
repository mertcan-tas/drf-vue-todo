from rest_framework import serializers
from api.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'memo', 'completed']
        extra_kwargs = {
            'memo': {'required': True}
        }
