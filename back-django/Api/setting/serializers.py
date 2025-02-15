from rest_framework import serializers
from .models import University, Major, Personnel, AdmissionPeriod

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name', 'level', 'created_at', 'updated_at']

class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ['id', 'name', 'category', 'created_at', 'updated_at']

class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = ['id', 'name', 'recruitment_type', 'created_at', 'updated_at']

class AdmissionPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionPeriod
        fields = ['id', 'start_date', 'end_date', 'created_at', 'updated_at']