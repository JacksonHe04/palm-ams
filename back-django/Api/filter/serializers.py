from rest_framework import serializers
from .models import FilterScheme

class FilterSchemeSerializer(serializers.ModelSerializer):
    conditions = serializers.ListField(required=True)

    class Meta:
        model = FilterScheme
        fields = ['id', 'name', 'enabled', 'conditions']
        read_only_fields = ['id']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['conditions'] = instance.get_conditions()
        return ret

    def create(self, validated_data):
        conditions = validated_data.pop('conditions', [])
        instance = super().create(validated_data)
        instance.set_conditions(conditions)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        conditions = validated_data.pop('conditions', [])
        instance = super().update(instance, validated_data)
        instance.set_conditions(conditions)
        instance.save()
        return instance