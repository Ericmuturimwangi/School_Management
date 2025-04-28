from rest_framework import serializers
from .models import SchoolClass, Attendance
from core.models import InstructorProfile

class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = ['id', 'name', 'assigned_instructor', 'subject']

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'student', 'school_class', 'date', 'status']

