from rest_framework import serializers
from .models import FilterScheme

class FilterSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilterScheme
        fields = ['id', 'name', 'config', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']