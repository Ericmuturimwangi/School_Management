from rest_framework import serializers
from .models import SchoolClass
from core.models import TeacherProfile

class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = ['__all__']
