from rest_framework import serializers
from .models import SchoolClass, Attendance
from core.models import InstructorProfile

class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = ['__all__']

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['__all__']

