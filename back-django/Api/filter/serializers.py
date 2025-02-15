from rest_framework import serializers
from .models import FilterScheme

class FilterSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilterScheme
        fields = '__all__' 