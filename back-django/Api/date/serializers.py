from rest_framework import serializers
from .models import AdmissionDate

class AdmissionDateSerializer(serializers.ModelSerializer):
    """
    招生时间配置序列化器
    """
    class Meta:
        model = AdmissionDate
        fields = ['id', 'year', 'type', 'start_time', 'end_time']